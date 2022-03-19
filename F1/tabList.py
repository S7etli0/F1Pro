from F1.mySQL import startSQL

mydb = startSQL(False)

def listSetRows(ref):

    curs = mydb.cursor()
    curs.execute("USE formula1db")
    curs.execute("SELECT * FROM " + ref)

    cellsdata = []
    vertic = []
    for x in curs:
        cellsdata.append(x[1:len(x)])
        vertic.append(str(x[0]))
    rows = len(cellsdata)

    mydb.commit()

    return cellsdata, vertic, rows
