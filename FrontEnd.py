import psycopg2
from datetime import datetime

def append_db(nimi,alku,loppu,projekti_nimi,selite,cursor):
    SQL = "INSERT INTO tyo_taulu (nimi,alku,loppu,projekti_nimi,selite) VALUES (%s,%s,%s,%s,%s);"
    data = (nimi,alku,loppu,projekti_nimi,selite)
    cursor.execute(SQL,data)

def kayttoliittyma():
    while (True):

        print("\n'Työmiehenkuolema'\n")

        nimi = input("Aloita syöttämällä käyttäjänimi: ")
        while (True):
            alkua = input("Aloitusaika YYYY/MM/DD HH:MM: ")
            try:
                alku = datetime.strptime(alkua, '%Y/%m/%d %H:%M')
            except:
                print("Virheellinen aikasyöte, tarkista formaatti (YYYY/MM/DD HH:MM)")
                continue
            break
  
        while (True):
            while(True):        
                loppua = input("Lopetusaika: YYYY/MM/DD HH:MM: ")

                try:
                    loppu = datetime.strptime(loppua, '%Y/%m/%d %H:%M')
                except:
                    print("Virheellinen aikasyöte, tarkista formaatti (YYYY/MM/DD HH:MM)")
                    continue
                break           

            if loppua < alkua:
                print("Lopetusaika ei saa olla aiemmin kuin aloitusaika.")
                continue
            elif loppua == alkua:
                print("Alku ja lopetusajat samat.")
            else:
                break

        projekti_nimi = input("projekti: ")
        selite = input("Tehdyt tehtävät: ")

        with open("./ignore.txt", 'r') as file:
            lines = [line.rstrip() for line in file]
        pw = lines[0]

        con = None
        try:
            con = psycopg2.connect("dbname=tyotunnit user=postgres password = {}".format(pw))
            cursor = con.cursor()

            append_db(nimi,alku,loppu,projekti_nimi,selite,cursor)

            con.commit()
            cursor.close()
            con.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
    
        print("Tiedot kirjattu!")

