from PyQt5.QtWidgets import QWidget, QVBoxLayout


def AddingItems(allitems,lay):
    for item in allitems:
        lay.addWidget(item)


def Visibility(allitems,check):
    for item in allitems:
        item.setVisible(check)


def layinWidget():
    wid = QWidget()
    lay = QVBoxLayout()
    wid.setLayout(lay)

    return wid,lay
