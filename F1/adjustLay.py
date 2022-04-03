from F1.itemSetter import layinWidget

class changeLay():
    def __init__(self,lay):
        self.lay = lay

    # remove all widgets inside the layout
    def clearLay(self):
        for i in reversed(range(self.lay.count())):
            if self.lay.itemAt(i).widget():
                self.lay.itemAt(i).widget().setParent(None)

    # add a stretch to the layout via widget
    def stretchLay(self):
        stretch, strlay = layinWidget()
        strlay.addStretch()
        self.lay.addWidget(stretch)



