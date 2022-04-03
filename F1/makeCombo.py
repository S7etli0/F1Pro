from PyQt5.QtWidgets import QLabel, QComboBox
from F1.itemSetter import changeItems


# create label & combobox to add them to layout
def setComboBox(check,sections,lay):
    if check == 1:
        x, y = "Set data:", "RedLab"
    elif check == 2:
        x, y = "Select year:", "BlackLab"
    else:
        x, y = "Sort Label:", "RedLab"

    datalbl = QLabel(x)
    datalbl.setObjectName(y)
    combo = QComboBox()
    combo.addItems(sections)

    changeItems([datalbl,combo]).AddingItems(lay)
    
    return datalbl, combo