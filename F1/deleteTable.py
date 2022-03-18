import mysql.connector as con
from PyQt5.QtWidgets import QMessageBox

mydb = con.connect(
    host="localhost",
    user="root",
    passwd="Slav7528dokumape"
)

def eraseTab(self, deltab):
    ask = QMessageBox.question(self, "Delete Table", "Do you want to drop table " + deltab + " ?",
                               QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    if ask == QMessageBox.Yes:
        curs = mydb.cursor()
        curs.execute("USE formula1db")
        curs.execute("DROP TABLE " + deltab)
        mydb.commit()
        QMessageBox.about(self, "Delete Table", "The table was erased from the database!")
        self.goBack()
    else:
        pass