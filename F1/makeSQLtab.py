from PyQt5.QtWidgets import QMessageBox
from F1.mySQL import startSQL


# use the data to create a SQL file
def createSQL(self, name, content, tabheader):

    mydb,curs = startSQL(False)
    cols = len(tabheader)
    rows = len(content)

    curs.execute("CREATE TABLE IF NOT EXISTS " + name + " (id int PRIMARY KEY AUTO_INCREMENT)")
    for x in range(cols):
        curs.execute("ALTER TABLE " + name + " ADD " + tabheader[x] + " VARCHAR(125)")

    rep = []
    for x in range(cols):
        rep.append("%s")

    datatag = str(tabheader)[1:-1].replace("'", "")
    datavalue = str(rep)[1:-1].replace("'", "")
    formula = "INSERT INTO " + name + " (" + datatag + ") VALUES (" + datavalue + ")"

    stock = []
    for x in range(rows):
        line = []
        for y in range(cols):
            line.append(content[x][y])
        stock.append(line)

    curs.executemany(formula, stock)
    mydb.commit()

    QMessageBox.about(self, "SQL Table", "Table " + name + " was added to the database!")