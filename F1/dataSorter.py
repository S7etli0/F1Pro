from F1.mySQL import startSQL


def sortData(dataref,sorter,direct):
    mydb,curs = startSQL(False)

    if sorter == "date" or sorter == "id" or sorter == "points":
        curs.execute("SELECT * FROM " + dataref + " ORDER BY id" + " " + direct)
    elif sorter == "laps":
        curs.execute("SELECT * FROM " + dataref + " ORDER BY ABS(" + sorter + ") " + direct)
    else:
        curs.execute("SELECT * FROM " + dataref + " ORDER BY " + sorter + " " + direct)

    cellsdata = []
    vertic = []
    for x in curs:
        cellsdata.append(x[1:len(x)])
        vertic.append(str(x[0]))

    return cellsdata, vertic

