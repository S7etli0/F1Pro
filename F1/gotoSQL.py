from PyQt5.QtCore import Qt
from F1.imageSet import tabImage
from F1.newWidget import layinWidget
from PyQt5.QtWidgets import QLabel, QPushButton


# open the SQL menu & choose a category
def backtoSQL(innerlay):

    sqltitel = QLabel("Choose a Table Category")
    sqltitel.setObjectName("BlackLab")
    sqltitel.setAlignment(Qt.AlignCenter)
    innerlay.addWidget(sqltitel)
    tabImage('sql-menu', 3, innerlay)

    sections = ['calendar', 'race_wins', 'driver_ranks', 'team_ranks']
    btnwid, btnlay = layinWidget("V")

    buttons = []
    for x in sections:
        btn = QPushButton(str(x))
        btn.setObjectName("RedBtn")
        btnlay.addWidget(btn)
        buttons.append(btn)

    btnwid.setObjectName("BlackWid")
    innerlay.addWidget(btnwid)

    return buttons