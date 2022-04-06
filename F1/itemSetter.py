class changeItems():
    def __init__(self,allitems):
        self.allitems = allitems

    # add widgets to a layout
    def AddingItems(self,lay):
        self.lay = lay
        for item in self.allitems:
            self.lay.addWidget(item)

    # change item visibility
    def Visibility(self,check):
        self.check = check
        for item in self.allitems:
            item.setVisible(self.check)



