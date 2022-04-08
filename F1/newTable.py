from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QScrollArea
from F1.newWidget import layinWidget


# create a table to display the data
def setTable(cols,rows):

    table = QTableWidget()
    table.setRowCount(rows)
    table.setColumnCount(cols)
    table.horizontalHeader().setStretchLastSection(True)

    tabwid, form = layinWidget("V")
    form.addWidget(table)

    scroll = QScrollArea()
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    form.addWidget(scroll)
    scroll.setVisible(False)

    return table, tabwid, scroll