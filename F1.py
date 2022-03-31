import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QTabWidget, QApplication, QProgressBar, QScrollArea, \
    QTableWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox

from F1.dataTitel import sqlTitel
from F1.imageSet import tabImage
from F1.cssLay import css_Style
from F1.loader import loadingData
from F1.dataScrape import WebScrape
from F1.tabList import listSetRows
from F1.height import tabHeight
from F1.loadBar import progressload
from F1.adjustLay import clearLay, stretchLay
from F1.deleteTable import eraseTab
from F1.asktoSave import SQLsave
from F1.dataSorter import sortData
from F1.tableFiller import fillTable
from F1.headerSQL import setSQLheader
from F1.allTabs import openTab
from F1.goingBack import backtoSQL
from F1.setYear import setYearLbl
from F1.makeCombo import setComboBox
from F1.tableWidth import tabWidth
from F1.sortOptions import sortItems
from F1.raceData import getRaceData
from F1.itemSetter import Visibility, AddingItems

# check whole page
# check modules
# make classes
# out methods, def
# remove repeats
# descriptions
# set values
# presentation

class DataF1Table(QWidget):
    def __init__(self):
        super().__init__()
        self.VisualTab()


    def VisualTab(self):
        self.setWindowTitle("Formula1 Database")
        self.setWindowIcon(QIcon("images/f1-logo.png"))
        self.setMaximumSize(925, 435)   #670
        self.move(100, 100)

        self.setObjectName("RedWid")
        self.gridStructure()
        self.mainVariables()
        self.setMainTab()
        self.sideWEBtab()
        self.show()


    def gridStructure(self):
        loadwid = QWidget()
        self.layload = QVBoxLayout()
        loadwid.setLayout(self.layload)

        loadlabl = QLabel("Scrape Data from the Website")
        loadlabl.setObjectName("BlackLab")
        loadlabl.setAlignment(Qt.AlignCenter)
        self.layload.addWidget(loadlabl)
        tabImage('menu', 3, self.layload)

        sqltabs = QWidget()
        self.innerlay = QVBoxLayout()
        sqltabs.setLayout(self.innerlay)

        maintab = QTabWidget()
        maintab.setMaximumWidth(270)
        maintab.addTab(loadwid, "Load Data")
        maintab.addTab(sqltabs, "View Data")

        tabright = QWidget()
        tabright.setObjectName("White")
        self.mainwid = QVBoxLayout()
        tabright.setLayout(self.mainwid)

        mygrid = QGridLayout()
        mygrid.addWidget(maintab, 0, 0)
        mygrid.addWidget(tabright, 0, 1)
        self.setLayout(mygrid)

        self.goBack()


    def mainVariables(self):
        self.tablemade = False
        self.sortbool = False
        self.changer=""
        
        self.eraselbl = QLabel()
        self.erase = QPushButton("Erase SQL Table")
        self.erase.clicked.connect(lambda:self.deletion())

        self.sortwid = QWidget()
        self.sortwid.setObjectName("BlackWid")
        self.sortlay = QHBoxLayout()
        self.sortlay.setAlignment(Qt.AlignCenter)


    def setMainTab(self):
        self.titel = QLabel("The Results You are Looking For will Appear in a Table")
        self.titel.setAlignment(Qt.AlignCenter)
        self.titel.setObjectName("Titel")
        
        self.introlbl = QLabel()
        tabImage('startup', 2, self.introlbl)
        self.tablay = QVBoxLayout()

        self.loadtab = QProgressBar()
        self.loadtab.setMinimum(0)
        self.loadtab.setMaximum(10)
        self.loadtab.setVisible(False)

        AddingItems([self.titel,self.introlbl],self.mainwid)
        self.mainwid.addLayout(self.tablay)
        AddingItems([self.sortwid,self.loadtab],self.mainwid)


    def sideWEBtab(self):
        firstrow = QHBoxLayout()
        self.spinlbl,self.spinyear = setYearLbl()
        firstrow.addWidget(self.spinlbl)
        firstrow.addWidget(self.spinyear)

        secrow = QHBoxLayout()
        sections = ['calendar', 'race wins', 'driver ranks', 'team ranks']
        self.datalbl,self.combo = setComboBox(1,sections)
        secrow.addWidget(self.datalbl)
        secrow.addWidget(self.combo)

        doubwid = QWidget()
        doubwid.setObjectName("BlackWid")
        doublay = QVBoxLayout()
        doubwid.setLayout(doublay)
        doublay.addLayout(firstrow)
        doublay.addLayout(secrow)

        btn = QPushButton("Load Data in Table")
        btn.setObjectName("Mar")
        btn.clicked.connect(self.race_results)

        self.savelbl = QLabel()
        tabImage('saves', 1, self.savelbl)
        self.savelbl.setVisible(False)

        self.savedata = QPushButton("Create SQL Table")
        self.savedata.clicked.connect(self.saving)
        self.mainwid.addWidget(self.savedata)
        self.savedata.setVisible(False)

        clearlab = QLabel()
        addtoLayload = [doubwid,btn,clearlab,self.savelbl,self.savedata]
        AddingItems(addtoLayload,self.layload)
        self.layload.addStretch()


    def race_results(self):
        if self.sortbool == True:
            clearLay(self.sortlay)
            self.sortbool = False
            Visibility([self.sortwid, self.erase,self.eraselbl],False)

        calendar = int(self.spinyear.text())
        data = str(self.combo.currentText())

        if data == "team ranks" and calendar < 1958:
            QMessageBox.about(self, "Data Error", "No team Competitions before 1958!")
        else:
            Visibility([self.savedata,self.savelbl],True)
            links, var, self.tabheader, cols, numbers = loadingData(data)

            for sector in links:
                table = WebScrape(calendar, sector)
                progressload(self.loadtab)
                self.content, rows = getRaceData(table,data,var,numbers,sector)

            if self.tablemade != False:
                self.tablay.removeWidget(self.tabwid)
            self.makeTable(cols,rows)
            self.tabwid.setObjectName("BlackWid")

            tabImage(data.replace(" ", "-"), 2, self.introlbl)
            self.titletext = data.title() + " for the " + str(calendar)
            self.titel.setText("List of the " + self.titletext + " Formula 1 Season")

            vertic = []
            for i in range(rows):
                vertic.append(str(i + 1))

            fillTable(self.table, self.content, self.tabheader, vertic)
            tabHeight(self, rows, self.sortbool)
            tabWidth(self,self.table,self.titel,self.scroll,self.tabwid)

        self.goBack()


    def getList(self):
        listname = self.sender().text()
        allcontent = openTab(listname)#.openTab_act()
        clearLay(self.innerlay)

        category = str(listname).replace("_", " ").title()
        maintag = QLabel("Category " + category + " Tables")

        maintag.setObjectName("BlackLab")
        maintag.setAlignment(Qt.AlignCenter)
        self.innerlay.addWidget(maintag)
        tabImage('menues', 3, self.innerlay)

        twoinone = QHBoxLayout()
        lbltag, self.yearlist = setComboBox(2,allcontent)
        twoinone.addWidget(lbltag)
        twoinone.addWidget(self.yearlist)

        twolinewid = QWidget()
        twolinewid.setObjectName("RedWid")
        twolinewid.setLayout(twoinone)

        btn = QPushButton("Load SQL Table")
        btn.clicked.connect(lambda:self.getSQLtab(allcontent,listname))

        backbtn = QPushButton("Back to Menu")
        backbtn.clicked.connect(self.goBack)

        clearlbl = QLabel()
        tabImage('btn-del', 1, self.eraselbl)

        addtoInnerLay = [twolinewid,btn,backbtn,clearlbl,self.eraselbl,self.erase]
        AddingItems(addtoInnerLay,self.innerlay)

        Visibility([self.eraselbl, self.erase], False)
        stretchLay(self.innerlay)


    def getSQLtab(self,allcontent,listname):

        if self.sortbool != True:
            self.sortbool = True
            Visibility([self.savedata, self.savelbl], False)

        if len(allcontent) == 0:
            QMessageBox.about(self,"Empty Database","No tables are Saved in this Category!")
        else:
            self.currtab = listname + "_" + str(self.yearlist.currentText())

            if self.tablemade != False:
                self.tablay.removeWidget(self.tabwid)

            cellsdata,vertic,rows = listSetRows(self.currtab)
            colname,cols = setSQLheader(self.currtab)
            self.makeTable(cols,rows)

            tabImage(listname.replace("_", "-"), 2, self.introlbl)
            titletext = sqlTitel(self.currtab)
            self.titel.setText(titletext)

            Visibility([self.erase,self.eraselbl],True)
            fillTable(self.table, cellsdata, colname, vertic)
            tabWidth(self,self.table,self.titel,self.scroll,self.tabwid)

            if listname!=self.changer:
                self.changer = listname
                clearLay(self.sortlay)
                self.sortbool = False

            if self.sortbool == False:
                self.resetSQLtab(colname)


    def resetSQLtab(self,colname):
        self.sortwid.setVisible(True)

        if "race" in self.currtab:
            colname.append('order')
        sortlbl, self.sortbox = setComboBox(3, colname)

        order, self.asc, self.des, sortbtn = sortItems()
        sortbtn.clicked.connect(lambda:self.sorting(colname))

        addtoSortlay = [sortlbl, self.sortbox, order, self.asc, self.des, sortbtn]
        AddingItems(addtoSortlay, self.sortlay)

        self.sortwid.setLayout(self.sortlay)
        self.sortbool = True


    def goBack(self):
        clearLay(self.innerlay)
        buttons = backtoSQL(self.innerlay)
        for btn in buttons:
            btn.clicked.connect(self.getList)
        stretchLay(self.innerlay)


    def makeTable(self,cols,rows):
        self.tablemade = True
        self.table = QTableWidget()
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.tabwid = QWidget()
        self.form = QVBoxLayout()
        self.form.addWidget(self.table)
        self.tabwid.setLayout(self.form)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.form.addWidget(self.scroll)
        self.scroll.setVisible(False)
        self.tablay.addWidget(self.tabwid)

        if self.sortbool == True:
            self.tabwid.setFixedHeight(370)
        tabHeight(self, rows, self.sortbool)


    def sorting(self, colname):
        if 'order' in colname:
            colname.remove('order')

        if self.asc.isChecked():
            direct = self.asc.text()
        else:
            direct = self.des.text()

        sorter = self.sortbox.currentText()
        cellsdata,vertic = sortData(self.currtab,sorter,direct)
        fillTable(self.table, cellsdata, colname, vertic)


    def deletion(self):
        ask = eraseTab(self,self.currtab)
        if ask==True:
            self.goBack()
            self.changer=""
            clearLay(self.sortlay)


    def saving(self):
        name = (self.titletext.replace(" for the ", "_")).replace(" ", "_")
        ask = SQLsave(self, name, self.content, self.tabheader)
        if ask == True:
            self.goBack()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(css_Style)
    window = DataF1Table()
    sys.exit(app.exec_())
