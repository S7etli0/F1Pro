import mysql.connector as con

def startSQL(check):
    mydb = con.connect(
        host="localhost",
        user="root",
        passwd="Slav7528dokumape"
    )

    if check == True:
        curs = mydb.cursor()
        curs.execute("CREATE DATABASE IF NOT EXISTS formula1db")
        mydb.commit()

    return mydb
