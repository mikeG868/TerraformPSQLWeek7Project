import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def runDBcode(DBcode):
    with open("./ignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
        pw = lines[0]

        #Db tiedot
        user = "postgres"
        SQL,dbname = DBcode

        con = None
        try:
            con = psycopg2.connect("dbname={} user={} password={}".format(dbname,user,pw))
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = con.cursor()

            cursor.execute(SQL)

            con.commit()
            cursor.close()
            con.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()


def create_db(newDBname):
    SQL = "CREATE DATABASE {};".format(newDBname)
    return SQL,"postgres"

def create_table(DBname):
    SQLtable_init ="CREATE TABLE tyo_taulu (\
        id              SERIAL PRIMARY KEY, \
        nimi            varchar(255) NOT NULL, \
        alku            TIMESTAMP NOT NULL, \
        loppu           TIMESTAMP NOT NULL, \
        projekti_nimi   varchar(255) NOT NULL, \
        selite          varchar NOT NULL\
        );"
    return SQLtable_init,DBname

if __name__ == '__main__':

    DBname = "tyotunnit200"
    runDBcode(create_db(DBname))
    runDBcode(create_table(DBname))
