from PyQt5.QtWidgets import QLabel, QComboBox

def setComboBox(check,sections):

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
    
    return datalbl, combo