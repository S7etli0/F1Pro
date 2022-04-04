from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


# change the image in the table widget
def tabImage(picname, look, addimg):
    intropic = QPixmap("images/f1-" + picname + ".jpg")
    wd, ln = 260, 110

    # delete or save img
    if look == 1:
        addimg.setPixmap(intropic.scaled(wd, ln, Qt.KeepAspectRatio))

    # data table picture
    elif look == 2:
        addimg.setPixmap(intropic)
        addimg.setAlignment(Qt.AlignCenter)

    # menu picture
    else:
        sqlpic = QLabel()
        sqlpic.setPixmap(intropic.scaled(wd, ln, Qt.KeepAspectRatio))
        sqlpic.setAlignment(Qt.AlignCenter)
        addimg.addWidget(sqlpic)