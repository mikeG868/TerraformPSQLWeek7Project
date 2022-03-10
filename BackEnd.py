import psycopg2
import datetime
import smtplib
from email.message import EmailMessage
import time

def puuttuuko_tyoaikoja(lista: list):

    projektiinLiitetyt = ['Matti', 'Ville', 'Anna', 'Mike', 'Pietari', 'Heini']
    projektiinLiitetyt.sort(key = len)
    lista.sort(key = len)

    kirjaus_puuttuu = []

    i = 0
    for arvo in projektiinLiitetyt:
        if arvo not in lista:
            kirjaus_puuttuu.append(arvo)
    
    return kirjaus_puuttuu

def append_db(nimi,alku,loppu,projekti_nimi,selite,cursor):
    SQL = "INSERT INTO tyo_taulu (nimi,alku,loppu,projekti_nimi,selite) VALUES (%s,%s,%s,%s,%s,%s);"
    data = (nimi,alku,loppu,projekti_nimi,selite)
    cursor.execute(SQL,data)

def haeSarakkeet(cursor, con):
    print("Haetaan työaikoja...")
    aloitus = time.strftime("%Y-%m-%d 00:00:00")
    lopetus = time.strftime("%Y-%m-%d 23:59:59")

    SQL = "select * from tyo_taulu where alku between %s and %s"
    data = (aloitus, lopetus)
    cursor.execute(SQL, data)
    row = cursor.fetchall()

    aikalista = []

    for rivi in row:
        aikalista.append(rivi[3] - rivi[2])
    
    mysum = datetime.timedelta()
    for i in aikalista:
        s = i.total_seconds()
        d = datetime.timedelta(seconds=int(s))
        mysum += d

    puuttuuko_tyoaikoja(row)
    kirjoitaRaportti(mysum, row)

def kirjoitaRaportti(summa: datetime.timedelta(), rivit: list):
    print("Kirjoitetaan raportti...")

    with open("tyoaikaraportti.txt", "w") as tiedosto:
        for i in rivit:
            rivi = f'{str(i[0])} {str(i[1])}\naloittanut: {str(i[2])}\nlopettanut: {str(i[3])}\nTunteja: {i[3]-i[2]}\nProjektissa: {str(i[4])}\nSelvitys: {str(i[5])}\n\n'
            tiedosto.write(rivi)
        tiedosto.write(f'Kokonaistunnit: {str(summa)}')
    
    laheta_sahkoposti()

def laheta_sahkoposti():
    print("Lähetetään sähköposti...")
    with open("C:\Viikko7projekti\ignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
    pw = lines[1]
    
    with open("tyoaikaraportti.txt") as fp:
        msg = EmailMessage()
        msg['From'] = "linna.anna@gmail.com"
        msg['To'] = "ville.jouhten@saunalahti.fi"
        msg['Subject'] = 'Työaikaraportti'
        msg.set_content(fp.read())
      

    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()
    server.login("waffeloine@gmail.com", pw)
    server.sendmail("linna.anna@gmail.com", "ville.jouhten@saunalahti.fi", msg.as_string())

    server.quit()

def db_connection():
    con = None
    try:
        sslmode = "require"
        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)

        con = psycopg2.connect(conn_string) 
        print("Yhdistetty tietokantaan...")
        cursor = con.cursor()
        con.commit()
        haeSarakkeet(cursor, con)
        cursor.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == "__main__":
    with open("C:\Viikko7projekti\DBfiles\DBignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
    password = lines[0]
    host = lines[1]
    user = lines[2]
    dbname = "tyotunnit_db"

    db_connection()