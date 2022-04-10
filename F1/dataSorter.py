from F1.mySQL import startSQL


# make list to sort the data from the table
def sortData(tabname,colname,way):
    mydb,curs = startSQL(False)
    listcheck = ["full_date","order","all_points"]

    if colname in listcheck:
        direct = "id"
    elif colname == "race_laps":
        direct = "ABS(" + colname + ")"
    else:
        direct = colname

    curs.execute("SELECT * FROM " + tabname + " ORDER BY " + direct + " " + way)

    cellsdata = []
    vertic = []
    for x in curs:
        cellsdata.append(x[1:len(x)])
        vertic.append(str(x[0]))

    return cellsdata, vertic

