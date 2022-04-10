import datetime
from PyQt5.QtWidgets import QLabel, QSpinBox
from F1.itemSetter import changeItems


# create label & spinbox to add them to layout
def setYearLbl(lay):
    spinlbl = QLabel("Set year:")
    spinlbl.setObjectName("RedLab")

    spinyear = QSpinBox()
    year = datetime.datetime.now().strftime("%Y")
    spinyear.setRange(1950, int(year))

    changeItems([spinlbl,spinyear]).AddingItems(lay)

    return spinlbl, spinyear, year