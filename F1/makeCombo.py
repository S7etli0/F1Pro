from PyQt5.QtWidgets import QLabel, QComboBox

def setComboBox(check,sections):

    if check == 1:
        x, y = "Set data:","RedLab"
    else:
        x, y = "Select year:","BlackLab"

    datalbl = QLabel(x)
    datalbl.setObjectName(y)
    combo = QComboBox()
    combo.addItems(sections)
    
    return datalbl,combo