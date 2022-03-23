from PyQt5.QtWidgets import QHeaderView

def tabWidth(self,table,titel,scroll,tabwid):
    header = table.horizontalHeader()
    tabcol = len(header)

    max = 75
    for j in range(tabcol):
        table.resizeColumnToContents(j)
        max += table.columnWidth(j)

    if 'Calendar' in titel.text():
        for i in range(tabcol):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    elif 'Team' in titel.text():
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setStretchLastSection(False)

    elif 'Driver' in titel.text():
        for i in range(tabcol-2):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        header.setSectionResizeMode(tabcol - 1, QHeaderView.ResizeToContents)

    else:
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    self.setGeometry(100, 100, 0, 0)
    if max <= 750:
        tabwid.setMinimumWidth(max)
        self.setFixedWidth(max + 350)
    else:
        scroll.setWidget(table)
        scroll.setVisible(True)
        table.setMinimumWidth(max)
        self.setFixedWidth(1050)
