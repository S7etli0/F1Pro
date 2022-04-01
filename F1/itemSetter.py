from PyQt5.QtWidgets import QWidget, QVBoxLayout


# add items to a widget
def AddingItems(allitems,lay):
    for item in allitems:
        lay.addWidget(item)


# change item visibility
def Visibility(allitems,check):
    for item in allitems:
        item.setVisible(check)


# set layout in widget
def layinWidget():
    wid = QWidget()
    lay = QVBoxLayout()
    wid.setLayout(lay)

    return wid,lay
