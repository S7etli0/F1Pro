from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout


# set layout in widget
def layinWidget(type):
    if type == "V" or type == "H":
        wid = QWidget()

        if type == "V":
            lay = QVBoxLayout()
        else:
            lay = QHBoxLayout()
        wid.setLayout(lay)

        return wid, lay