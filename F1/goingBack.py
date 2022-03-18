from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from F1.images import tabImage

def backtoSQL(innerlay):
    sqltitel = QLabel("Choose a Table Category")
    sqltitel.setObjectName("BlackLab")
    sqltitel.setAlignment(Qt.AlignCenter)
    innerlay.addWidget(sqltitel)
    tabImage('menues', 3, innerlay)

    sections = ['calendar', 'race_wins', 'driver_ranks', 'team_ranks']
    btnlay = QVBoxLayout()
    for x in sections:
        btn = QPushButton(str(x))
        btn.setObjectName("RedBtn")
        btn.clicked.connect(self.getList)
        btnlay.addWidget(btn)

    btnwid = QWidget()
    btnwid.setObjectName("BlackWid")
    btnwid.setLayout(btnlay)
    innerlay.addWidget(btnwid)