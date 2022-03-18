from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem


def fillTable(table, tabrow, tabcol, filler, myheader, vertic):
    table.setRowCount(tabrow)
    table.setColumnCount(tabcol)
    table.setVerticalHeaderLabels(vertic)

    color = QColor(190, 190, 190)
    for rw in range(tabrow):
        for cl in range(tabcol):
            table.setItem(rw, cl, QTableWidgetItem(str(filler[rw][cl])))
            if rw % 2 == 0:
                table.item(rw, cl).setBackground(color)

    style = "::section {background-color: red; color:white; font-size: 12pt; font-weight:bold;}"

    header = table.horizontalHeader()
    header.setFixedHeight(40)
    table.setHorizontalHeaderLabels(myheader)
    header.setDefaultAlignment(Qt.AlignHCenter)
    header.setStyleSheet(style)

    sidehead = table.verticalHeader()
    sidehead.setFixedWidth(35)
    sidehead.setDefaultAlignment(Qt.AlignCenter)
    sidehead.setStyleSheet(style)
