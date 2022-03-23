def AddingItems(allitems,lay):
    for item in allitems:
        lay.addWidget(item)

def Visibility(allitems,check):
    for item in allitems:
        item.setVisible(check)
