import datetime
from PyQt5.QtWidgets import QLabel, QSpinBox

def setYearLbl():
    spinlbl = QLabel("Set year:")
    spinlbl.setObjectName("RedLab")
    spinyear = QSpinBox()
    year = datetime.datetime.now().strftime("%Y")
    spinyear.setRange(1950, int(year) - 1)

    return spinlbl,spinyear