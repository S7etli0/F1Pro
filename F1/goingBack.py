from PyQt5.QtCore import Qt
from F1.imageSet import tabImage
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

def backtoSQL(innerlay):
    sqltitel = QLabel("Choose a Table Category")
    sqltitel.setObjectName("BlackLab")
    sqltitel.setAlignment(Qt.AlignCenter)
    innerlay.addWidget(sqltitel)
    tabImage('menues', 3, innerlay)

    buttons = []
    sections = ['calendar', 'race_wins', 'driver_ranks', 'team_ranks']
    btnlay = QVBoxLayout()
    for x in sections:
        btn = QPushButton(str(x))
        btn.setObjectName("RedBtn")
        btnlay.addWidget(btn)
        buttons.append(btn)

    btnwid = QWidget()
    btnwid.setObjectName("BlackWid")
    btnwid.setLayout(btnlay)
    innerlay.addWidget(btnwid)

    return buttons