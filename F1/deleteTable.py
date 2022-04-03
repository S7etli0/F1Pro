from PyQt5.QtWidgets import QMessageBox
from F1.mySQL import startSQL


# SQL command for dropping a file
class eraseTab():
    def __init__(self,lay, deltab):
        self.lay = lay
        self.deltab = deltab

    def asktoclear(self):
        ask = QMessageBox.question(self.lay, "Delete Table", "Do you want to drop table " + self.deltab + " ?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if ask == QMessageBox.Yes:
            mydb, curs = startSQL(False)
            curs.execute("DROP TABLE " + self.deltab)
            mydb.commit()
            QMessageBox.about(self.lay, "Delete Table", "Table " + self.deltab + " was erased from the database!")
            ask = True
        else:
            ask = False

        return ask