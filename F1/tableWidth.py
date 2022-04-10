from PyQt5.QtWidgets import QHeaderView
from F1.width import layWidth


# resize the table sections and adjust the table width
def tabWidth(self,table,titel,scroll,tabwid):

    header = table.horizontalHeader()
    tabcol = len(header)
    titel = titel.text()

    max = layWidth(table).sections(tabcol)

    if 'Team' in titel:
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setStretchLastSection(False)

    else:
        x = [2]
        if 'Driver' in titel:
            x = [0,2]

        for i in range(tabcol):
            if i in x:
                continue
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    layWidth(table).fixedWidth(self,scroll,tabwid,max)