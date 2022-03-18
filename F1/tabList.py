import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    passwd="Slav7528dokumape"
)

def listSetRows(ref,check):
    if check == True:
        curs = mydb.cursor()
        curs.execute("USE formula1db")
        curs.execute("SELECT * FROM " + ref)
    else:
        curs = ref

    cellsdata = []
    vertic = []
    for x in curs:
        cellsdata.append(x[1:len(x)])
        vertic.append(str(x[0]))
    rows = len(cellsdata)

    return cellsdata, vertic, rows