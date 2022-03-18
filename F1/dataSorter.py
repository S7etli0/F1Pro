import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    passwd="Slav7528dokumape"
)


def sortData(sorter,dataref,direct):
    curs = mydb.cursor()
    curs.execute("USE formula1db")
    if sorter == "date" or sorter == "id" or sorter == "points":
        curs.execute("SELECT * FROM " + dataref + " ORDER BY id" + " " + direct)
    elif sorter == "laps":
        curs.execute("SELECT * FROM " + dataref + " ORDER BY ABS(" + sorter + ") " + direct)
    else:
        curs.execute("SELECT * FROM " + dataref + " ORDER BY " + sorter + " " + direct)

    return curs
