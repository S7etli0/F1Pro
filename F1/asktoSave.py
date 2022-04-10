from PyQt5.QtWidgets import QMessageBox
from F1.makeSQLtab import createSQL
from F1.mySQL import startSQL


# ask to save and check if the file exists
def SQLsave(self, name, content, tabheader, limit):

    z = len(name)
    name = str(name).lower()
    category = name[0:z-5]

    ask = QMessageBox.question(self, "Saving Table", "Do you want to save table " + name + " ?",
                               QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    if ask == QMessageBox.Yes:
        mydb,curs = startSQL(True)
        curs.execute("SHOW TABLES")

        alltables = []
        for x in curs:
            clear = str(x)[2:-3]
            if category in clear:
                alltables.append(clear)

        # send data to create SQL file
        ask = False
        if name not in alltables:
            if str(limit) not in name:
                createSQL(self, name, content, tabheader)
                ask = True
            else:
                QMessageBox.about(self, "SQL error", "Can't save, season still in progress!")
        else:
            QMessageBox.about(self, "SQL error", "Table " + name + " is already in the database!")
    else:
        ask = False

    return ask
