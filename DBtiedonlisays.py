import psycopg2

def append_db(localfilename,container,blob,URL,cursor):
    SQL = "INSERT INTO blob1 (localfilename, BLOB_CONTAINER, blob_name, containerURL) VALUES (%s,%s,%s,%s);"
    data = (localfilename,container,blob,URL)
    cursor.execute(SQL,data)

if __name__ == '__main__':

    with open("./ignore.txt", 'r') as file:
        lines = [line.rstrip() for line in file]
    cstr = lines[0]
    pw = lines[1]

    storage_name = "mikestorageacademy"
    BLOB_CONTAINER = "mikecontainer"
    blob_name = "picture.png"
    localfilename = "./src/picture.png"
    containerURL = "https://"+storage_name+".blob.core.windows.net/"+BLOB_CONTAINER

    #uploadfile(BLOB_CONTAINER,blob_name,cstr,localfilename)

    con = None
    try:
        con = psycopg2.connect("dbname=blobdb user=postgres password = {}".format(pw))
        cursor = con.cursor()

        append_db(localfilename,BLOB_CONTAINER,blob_name,containerURL,cursor)

        con.commit()
        cursor.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
