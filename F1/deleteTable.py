from PyQt5.QtWidgets import QMessageBox
from F1.mySQL import startSQL


def eraseTab(lay, deltab):
    ask = QMessageBox.question(lay, "Delete Table", "Do you want to drop table " + deltab + " ?",
                               QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    if ask == QMessageBox.Yes:
        mydb = startSQL(False)
        curs = mydb.cursor()
        curs.execute("USE formula1db")
        curs.execute("DROP TABLE " + deltab)
        QMessageBox.about(lay, "Delete Table", "The table was erased from the database!")
        ask = True
    else:
        ask = False

    return ask
