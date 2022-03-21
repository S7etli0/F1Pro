from PyQt5.QtWidgets import QWidget, QVBoxLayout


def clearLay(lay):
    for i in reversed(range(lay.count())):
        if lay.itemAt(i).widget():
            lay.itemAt(i).widget().setParent(None)


def stretchLay(lay):
    stretch = QWidget()
    strlay = QVBoxLayout()
    strlay.addStretch()
    stretch.setLayout(strlay)
    lay.addWidget(stretch)
