from F1.mySQL import startSQL

def openTab(name):
    mydb = startSQL(True)
    curs = mydb.cursor()
    curs.execute("USE formula1db")
    curs.execute("SHOW TABLES")

    allcontent = []
    for x in curs:
        titel = str(x)[1:-1].replace(",", "")
        if name in titel:
            allcontent.append(titel.replace("'", "")[len(titel) - 6:len(titel)])

    return allcontent