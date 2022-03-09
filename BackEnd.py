import psycopg2
import datetime
import smtplib
from email.message import EmailMessage



# def append_db(nimi,alku,loppu,projekti_nimi,selite,cursor):
#     SQL = "INSERT INTO tyo_taulu (nimi,alku,loppu,projekti_nimi,selite) VALUES (%s,%s,%s,%s,%s);"
#     data = (nimi,alku,loppu,projekti_nimi,selite)
#     cursor.execute(SQL,data)

# def haeSarakkeet(cursor, con):

#     SQL = "select * from tyo_taulu where alku between '2000-12-30 10:00' and '2000-12-30 12:00'"
#     cursor.execute(SQL)
#     row = cursor.fetchall()

#     aikalista = []

#     for rivi in row:
#         aikalista.append(rivi[3] - rivi[2])

#     # for rivi in aikalista:
#     #     print(rivi.total_seconds())
    
#     mysum = datetime.timedelta()
#     for i in aikalista:
#         s = i.total_seconds()
#         d = datetime.timedelta(seconds=int(s))
#         mysum += d

#     print(mysum)

# with open("./ignore.txt", 'r') as file:
#     lines = [line.rstrip() for line in file]
# pw = lines[0]

# con = None
# try:
#     con = psycopg2.connect("dbname=tyotunnit user=postgres password = {}".format(pw))
#     cursor = con.cursor()

#     haeSarakkeet(cursor, con)

#     con.commit()
#     cursor.close()
#     con.close()

# except (Exception, psycopg2.DatabaseError) as error:
#     print(error)
# finally:
#     if con is not None:
#         con.close()

######
with open("./ignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
        pw = lines[0]


""" with open("tyoaikaraportti.txt", "w") as tiedosto:
    for i in data['items']:
        tiedosto.write(i['parameter'])
        tiedosto.write("\n")    
           """


# Luodaan tesktitiedostosta viesti
with open("tyoaikaraportti.txt") as fp:
    msg = EmailMessage()
    msg['From'] = "linna.anna@gmail.com"
    msg['To'] = "ville.jouhten@saunalahti.fi"
    msg['Subject'] = 'Työaikaraportti'
    msg.set_content(fp.read())
      


server = smtplib.SMTP('smtp.gmail.com', 587) 
server.starttls()
server.login("linna.anna", pw)
#msg = "The count in the table is currently this many rows " # message
server.sendmail("linna.anna@gmail.com", "ville.jouhten@saunalahti.fi", msg.as_string())

server.quit()