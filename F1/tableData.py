from F1.mySQL import startSQL


# get the content of SQL file minus colheader
def listSetRows(ref):
    mydb,curs = startSQL(False)
    curs.execute("SELECT * FROM " + ref)

    cellsdata = []
    vertic = []
    for x in curs:
        cellsdata.append(x[1:len(x)])
        vertic.append(str(x[0]))
    rows = len(cellsdata)

    return cellsdata, vertic, rows