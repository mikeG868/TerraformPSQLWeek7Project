import psycopg2
from datetime import datetime

def append_db(nimi,alku,loppu,projekti_nimi,selite,cursor):
    SQL = "INSERT INTO tyo_taulu (nimi,alku,loppu,projekti_nimi,selite) VALUES (%s,%s,%s,%s,%s);"
    data = (nimi,alku,loppu,projekti_nimi,selite)
    cursor.execute(SQL,data)


if __name__ == '__main__':

    with open("./ignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
    pw = lines[0]

    nimi = 'matti'
    alku = '2011-10-16 15:36:38'
    loppu = '2011-10-22 15:36:38'
    projekti_nimi = 'blabla'
    selite = 'blablabla'

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
