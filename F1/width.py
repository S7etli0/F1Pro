# adjust the table width & other items
class layWidth():
    def __init__(self,table):
        self.table = table

    def sections(self, tabcol):
        max = 75
        for j in range(tabcol):
            self.table.resizeColumnToContents(j)
            max += self.table.columnWidth(j)
        return max

    def fixedWidth(self, lay, scroll, tabwid, max):
        lay.setGeometry(100, 100, 0, 0)
        if max <= 700:
            tabwid.setMinimumWidth(max)
            lay.setFixedWidth(max + 350)
        else:
            scroll.setWidget(self.table)
            scroll.setVisible(True)
            self.table.setMinimumWidth(max)
            lay.setFixedWidth(1050)


