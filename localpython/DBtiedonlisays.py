import psycopg2

#adds one row of work data to table
def append_table(tablename,dbname):
    #taulu tiedot
    nimi = 'matti'
    alku = '2011-10-16 15:36:38'
    loppu = '2011-10-24 15:36:38'
    projekti_nimi = 'blabla'
    selite = 'blablabla'
    saa = '-202.22'
    SQL = "INSERT INTO {} (nimi,alku,loppu,projekti_nimi,selite,saa) \
                    VALUES (%s,%s,%s,%s,%s,%s);".format(tablename)
    data = (nimi,alku,loppu,projekti_nimi,selite,saa)
    print('Running INSERT INTO')
    return SQL,data,dbname

#DBcode contains (SQL statement, data fields, target database)
def runDBcode(DBcode):
    with open("./ignore.txt", 'r') as file:
        #Db password
        lines = [line.rstrip() for line in file]
    pw = lines[0]

    #Db info
    user = "postgres"
    SQL,data,dbname = DBcode

    #Db connect and execute SQL code
    con = None
    try:
        con = psycopg2.connect("dbname={} user={} password={}".format(dbname,user,pw))
        cursor = con.cursor()

        cursor.execute(SQL,data)

        con.commit()
        cursor.close()
        con.close()
        print("Executed SQL code")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == '__main__':

    dbname = "tyotunnit_db"
    dbname.lower()
    tablename = "tyo_taulu"
    tablename.lower()

    runDBcode(append_table(tablename,dbname))
