from PyQt5.QtWidgets import QLabel, QRadioButton, QButtonGroup, QComboBox, QPushButton


def sortItems(colname,ref):
    sortlbl = QLabel("Sort Label:")
    sortlbl.setObjectName("RedLab")
    sortbox = QComboBox()

    if "race" in ref:
        colname.append("id")
    sortbox.addItems(colname)

    order = QLabel("Order by:")
    order.setObjectName("RedLab")
    asc = QRadioButton("ASC")
    asc.setChecked(True)
    des = QRadioButton("DESC")


    sortbtn = QPushButton("  Sort Data  ")
    sortbtn.setObjectName("RedBtn")
    
    return sortlbl, sortbox, order, asc, des, sortbtn