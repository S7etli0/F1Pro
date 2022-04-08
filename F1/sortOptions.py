from PyQt5.QtWidgets import QLabel, QRadioButton, QPushButton


# items for the sorting menu
def sortItems():
    order = QLabel("Order by:")
    order.setObjectName("RedLab")

    asc = QRadioButton("ASC")
    asc.setChecked(True)
    des = QRadioButton("DESC")

    sortbtn = QPushButton("  Sort Data  ")
    sortbtn.setObjectName("RedBtn")
    
    return order, asc, des, sortbtn