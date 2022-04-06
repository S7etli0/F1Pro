from F1.mySQL import startSQL


# list the names of SQL tables in the chosen category
def openTab(category):
    mydb, curs = startSQL(True)
    curs.execute("SHOW TABLES")

    allcontent = []
    for x in curs:
        titel = str(x)[2:-3]

        if category in titel:
            z = len(titel)
            allcontent.append(titel[z - 4:z])

    return allcontent

