from PyQt5.QtWidgets import QMessageBox
from F1.makeSQLtab import createSQL
from F1.mySQL import startSQL

mydb = startSQL(True)

def SQLsave(self, name, content, tabheader):

    ask = QMessageBox.question(self, "Saving Table", "Do you want to save table " + name + " ?",
                               QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    if ask == QMessageBox.Yes:

        curs = mydb.cursor()
        curs.execute("USE formula1db")
        curs.execute("SHOW TABLES")

        alltables = []
        for x in curs:
            clear = (str(x)[1:-1].replace(",", ""))
            alltables.append(clear.replace("'", ""))
        mydb.commit()

        if name not in alltables:
            createSQL(self, name, content, tabheader)
            ask = True
        else:
            QMessageBox.about(self, "SQL error", "Table " + name + " is already in the database!")
            ask = False
    else:
        ask = False

    return ask

    mydb.commit()