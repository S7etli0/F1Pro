from PyQt5.QtWidgets import QMessageBox
from F1.mySQL import startSQL


# use the data to create a SQL file
def createSQL(self, name, content, tabheader):
    mydb,curs = startSQL(False)
    cols = len(tabheader)

    rep = []
    curs.execute("CREATE TABLE IF NOT EXISTS " + name + " (id int PRIMARY KEY AUTO_INCREMENT)")
    for x in range(cols):
        curs.execute("ALTER TABLE " + name + " ADD " + tabheader[x] + " VARCHAR(125)")
        rep.append("%s")

    datatag = str(tabheader)[1:-1].replace("'", "")
    datavalue = str(rep)[1:-1].replace("'", "")
    formula = "INSERT INTO " + name + " (" + datatag + ") VALUES (" + datavalue + ")"

    curs.executemany(formula, content)
    mydb.commit()

    QMessageBox.about(self, "SQL Table", "Table " + name + " was added to the database!")