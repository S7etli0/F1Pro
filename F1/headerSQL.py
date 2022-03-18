import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    passwd="Slav7528dokumape"
)

def setSQLheader(ref):
    curs = mydb.cursor()
    curs.execute("USE formula1db")

    colname = []
    curs = mydb.cursor()
    curs.execute("SHOW COLUMNS FROM " + ref)
    for x in curs:
        colname.append(list(x)[0])
    colname.pop(0)
    cols = len(colname)

    return colname, cols


    