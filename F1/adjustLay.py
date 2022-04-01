from F1.itemSetter import layinWidget


# remove all widgets inside the layout
def clearLay(lay):
    for i in reversed(range(lay.count())):
        if lay.itemAt(i).widget():
            lay.itemAt(i).widget().setParent(None)


# add a stretch to the layout via widget
def stretchLay(lay):
    stretch, strlay = layinWidget()
    strlay.addStretch()
    lay.addWidget(stretch)
