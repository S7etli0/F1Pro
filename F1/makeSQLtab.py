import mysql.connector as con
from PyQt5.QtWidgets import QMessageBox

mydb = con.connect(
    host="localhost",
    user="root",
    passwd="Slav7528dokumape"
)

def createSQL(self, name, content, tabheader):
    stock = []
    curs = mydb.cursor()
    curs.execute("USE formula1db")
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

    for x in range(rows):
        line = []
        for y in range(cols):
            line.append(content[x][y])
        stock.append(line)

    curs.executemany(formula, stock)
    mydb.commit()

    QMessageBox.about(self, "SQL Table", "Table " + name + " was added to the database!")