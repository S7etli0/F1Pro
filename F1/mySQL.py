import mysql.connector as con
from F1.configParser import readConfig

file=".venv/config.ini"
section='mySQL'
data = readConfig(file,section)

def startSQL(check):

    mydb = con.connect(
        host=data["host"],
        user=data["user"],
        password=data["password"]
    )

    if check == True:
        curs = mydb.cursor()
        curs.execute("CREATE DATABASE IF NOT EXISTS formula1db")
        mydb.commit()

    curs = mydb.cursor()
    curs.execute("USE formula1db")

    return mydb, curs
