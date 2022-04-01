import datetime
from PyQt5.QtWidgets import QLabel, QSpinBox


# create label & spinbox to add them to layout
def setYearLbl(lay):
    spinlbl = QLabel("Set year:")
    spinlbl.setObjectName("RedLab")

    spinyear = QSpinBox()
    year = datetime.datetime.now().strftime("%Y")
    spinyear.setRange(1950, int(year) - 1)

    lay.addWidget(spinlbl)
    lay.addWidget(spinyear)

    return spinlbl,spinyear