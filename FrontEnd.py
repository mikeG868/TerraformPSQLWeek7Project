import psycopg2
from datetime import datetime

def append_db(nimi,alku,loppu,projekti_nimi,selite,cursor):
    SQL = "INSERT INTO tyo_taulu (nimi,alku,loppu,projekti_nimi,selite) VALUES (%s,%s,%s,%s,%s);"
    data = (nimi,alku,loppu,projekti_nimi,selite)
    cursor.execute(SQL,data)


while (True):

    print("\n'Työmiehenkuolema'\n")

    nimi = input("Aloita syöttämällä käyttäjänimi: ")
    while (True):
        alkua = input("Aloitusaika YYYY/MM/DD HH:MM: ")
        try:
            test = datetime.strptime(alkua, '%Y/%m/%d %H:%M')
        except:
            print("Vituiks meni.")
            continue
        break
  
    while (True):
        while(True):        
            loppua = input("Lopetusaika: YYYY/MM/DD HH:MM: ")

            try:
                test = datetime.strptime(loppua, '%Y/%m/%d %H:%M')
            except:
                print("Vituiks meni.")
                continue
            break           

        if loppua < alkua:
            print("Virheellinen aikasyöte: alkuaika myöhemmin kuin lopetus!")
            continue
        elif loppua == alkua:
            print("Alku ja lopetusajat samat.")
        else:
            break

    projekti_nimi = input("projekti: ")
    selite = input("Tehdyt tehtävät: ")

    # nimi = "abba"
    # alkua = "2002/12/30 11:00"
    # loppua = "2000/12/30 11:00"
    # projekti_nimi = "testtt"
    # selite = "selitys"

    # with open("./ignore.txt", 'r') as file:
    #     lines = [line.rstrip() for line in file]
    # pw = lines[0]

    alku = datetime.strptime(alkua, '%Y/%m/%d %H:%M')
    loppu = datetime.strptime(loppua, '%Y/%m/%d %H:%M')

    print(alku, loppu)

    # con = None
    # try:
    #     con = psycopg2.connect("dbname=tyotunnit user=postgres password = {}".format(pw))
    #     cursor = con.cursor()

    #     append_db(nimi,alku,loppu,projekti_nimi,selite,cursor)

    #     con.commit()
    #     cursor.close()
    #     con.close()

    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error)
    # finally:
    #     if con is not None:
    #         con.close()
    
    print("Tiedot kirjattu!")

