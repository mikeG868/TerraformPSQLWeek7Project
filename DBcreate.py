import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#DBcode contains (SQL statement,target database)
def runDBcode(DBcode):
    with open("./ignore.txt", 'r') as file:
        #Db password
        lines = [line.rstrip() for line in file]
        pw = lines[0]

        #Db info
        user = "postgres"
        SQL,dbname = DBcode

        #Db connect and execute SQL code
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

#returns SQL statement and target database
def create_db(newDBname):
    SQL = "CREATE DATABASE {};".format(newDBname)
    return SQL,"postgres"

#returns SQL statement and target database
def create_table(DBname,tablename):
    SQLtable_init ="CREATE TABLE {} (\
        id              SERIAL PRIMARY KEY, \
        nimi            varchar(255) NOT NULL, \
        alku            TIMESTAMP NOT NULL, \
        loppu           TIMESTAMP NOT NULL, \
        projekti_nimi   varchar(255) NOT NULL, \
        selite          varchar NOT NULL\
        );".format(tablename)
    return SQLtable_init,DBname


if __name__ == '__main__':

    dbname = "tyotunnit_db"
    dbname.lower()
    tablename = "tyo_taulu"
    tablename.lower()
    runDBcode(create_db(dbname))
    runDBcode(create_table(dbname,tablename))
