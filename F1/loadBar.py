import time

# loading the progress bar
class progressload():
    def __init__(self,loadtab,num):
        self.num = num
        self.loadtab = loadtab

    def activate(self):
        self.loadtab.setMinimum(0)
        self.loadtab.setMaximum(self.num)

        bars = self.num + 2
        while bars:
            time.sleep(0.15)
            bars -= 1
            self.loadtab.setVisible(True)

            if bars != 0:
                self.loadtab.setValue(self.num + 1 - bars)
            else:
                self.loadtab.setVisible(False)