from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem


# input data in the table rows and the headers
def fillTable(table, filler, myheader, vertic):
    tabrow = len(filler)
    tabcol = len(myheader)

    table.setRowCount(tabrow)
    table.setColumnCount(tabcol)
    table.setVerticalHeaderLabels(vertic)

    color = QColor(190, 190, 190)
    for rw in range(tabrow):
        for cl in range(tabcol):
            table.setItem(rw, cl, QTableWidgetItem(str(filler[rw][cl])))
            if rw % 2 == 0:
                table.item(rw, cl).setBackground(color)

    header = table.horizontalHeader()
    header.setFixedHeight(40)
    table.setHorizontalHeaderLabels(myheader)
    header.setDefaultAlignment(Qt.AlignHCenter)

    sidehead = table.verticalHeader()
    sidehead.setFixedWidth(35)
    sidehead.setDefaultAlignment(Qt.AlignCenter)

    style = "::section {background-color: red; color:white; font-size: 12pt; font-weight:bold;}"
    for h in [header,sidehead]:
        h.setStyleSheet(style)