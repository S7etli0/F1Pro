import mysql.connector as con
from F1.configParser import readConfig


# create and use database
file=".venv/config.ini"
section='mySQL'
data = readConfig(file,section)


def startSQL(check):

    mydb = con.connect(
        host=data["host"],
        user=data["user"],
        password=data["password"]
    )

    db = "formula1db"
    if check == True:
        curs = mydb.cursor()
        curs.execute("CREATE DATABASE IF NOT EXISTS "+db)
        mydb.commit()

    curs = mydb.cursor()
    curs.execute("USE "+db)

    return mydb, curs
