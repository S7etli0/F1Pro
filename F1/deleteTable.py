from PyQt5.QtWidgets import QMessageBox
from F1.mySQL import startSQL


def eraseTab(lay, deltab):
    ask = QMessageBox.question(lay, "Delete Table", "Do you want to drop table " + deltab + " ?",
                               QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    if ask == QMessageBox.Yes:
        mydb,curs = startSQL(False)
        curs.execute("DROP TABLE " + deltab)
        mydb.commit()
        QMessageBox.about(lay, "Delete Table", "Table " + deltab + " was erased from the database!")
        ask = True
    else:
        ask = False

    return ask