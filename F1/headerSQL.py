from F1.mySQL import startSQL


# get column names / count from a SQL file
def setSQLheader(ref):
    mydb,curs = startSQL(False)

    colname = []
    curs = mydb.cursor()
    curs.execute("SHOW COLUMNS FROM " + ref)
    for x in curs:
        colname.append(list(x)[0])
    colname.pop(0)
    cols = len(colname)

    return colname, cols
