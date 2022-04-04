from PyQt5.QtWidgets import QHeaderView
from F1.width import layWidth


# resize the table sections and adjust the table width
def tabWidth(self,table,titel,scroll,tabwid):
    header = table.horizontalHeader()
    tabcol = len(header)
    titel = titel.text()

    max = layWidth(table).sections(tabcol)

    if 'Calendar' in titel:
        for i in range(tabcol):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    elif 'Team' in titel:
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setStretchLastSection(False)

    elif 'Driver' in titel:
        for i in range(tabcol-2):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        header.setSectionResizeMode(tabcol - 1, QHeaderView.ResizeToContents)

    else:
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    layWidth(table).fixedWidth(self,scroll,tabwid,max)