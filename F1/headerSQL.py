from F1.mySQL import startSQL


def setSQLheader(ref):
    mydb = startSQL(False)
    curs = mydb.cursor()
    curs.execute("USE formula1db")

    colname = []
    curs = mydb.cursor()
    curs.execute("SHOW COLUMNS FROM " + ref)
    for x in curs:
        colname.append(list(x)[0])
    colname.pop(0)
    cols = len(colname)

    mydb.commit()

    return colname, cols
