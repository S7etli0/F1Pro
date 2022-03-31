from F1.itemSetter import layinWidget


def clearLay(lay):
    for i in reversed(range(lay.count())):
        if lay.itemAt(i).widget():
            lay.itemAt(i).widget().setParent(None)


def stretchLay(lay):
    stretch, strlay = layinWidget()
    strlay.addStretch()
    lay.addWidget(stretch)
