import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QTabWidget, QApplication, QProgressBar, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox


# list of the modules used by the main class
from F1.dataTitel import sqlTitel
from F1.imageSet import tabImage
from F1.cssLay import css_Style
from F1.loader import loadingData
from F1.dataScrape import WebScrape
from F1.tableData import listSetRows
from F1.height import tabHeight
from F1.loadBar import progressload
from F1.adjustLay import changeLay
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
from F1.newTable import setTable
from F1.itemSetter import changeItems
from F1.newWidget import layinWidget


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
        loadwid, self.layload = layinWidget("V")
        sqltabs, self.innerlay = layinWidget("V")

        maintab = QTabWidget()
        maintab.setMaximumWidth(270)
        maintab.addTab(loadwid, "Load Data")
        maintab.addTab(sqltabs, "View Data")

        tabright, self.mainwid = layinWidget("V")
        tabright.setObjectName("White")

        mygrid = QGridLayout()
        mygrid.addWidget(maintab, 0, 0)
        mygrid.addWidget(tabright, 0, 1)
        self.setLayout(mygrid)

        self.goBack()


    # settings for the SQL menu
    def mainVariables(self):
        self.tablemade = False
        self.sortbool = False
        self.changer=""

        self.eraselbl = QLabel()
        tabImage('btn-del', 1, self.eraselbl)
        self.erase = QPushButton("Erase SQL Table")
        self.erase.clicked.connect(lambda:self.deletion())

        self.sortwid,self.sortlay = layinWidget("H")
        self.sortwid.setObjectName("BlackWid")
        self.sortlay.setAlignment(Qt.AlignCenter)
        self.sortwid.setVisible(False)


    # layout for displaying data in a table format
    def setMainTab(self):
        self.titel = QLabel("The Results You are Looking For will Appear in a Table")
        self.titel.setAlignment(Qt.AlignCenter)
        self.titel.setObjectName("Titel")

        self.introlbl = QLabel()
        tabImage('startup', 2, self.introlbl)
        self.tablay = QVBoxLayout()

        self.loadtab = QProgressBar()
        self.loadtab.setVisible(False)
        changeItems([self.titel,self.introlbl]).AddingItems(self.mainwid)
        self.mainwid.addLayout(self.tablay)
        changeItems([self.sortwid,self.loadtab]).AddingItems(self.mainwid)


    # menu for scraping data about F1
    def sideWEBtab(self):
        loadlabl = QLabel("Scrape Data from the Website")
        loadlabl.setObjectName("BlackLab")
        loadlabl.setAlignment(Qt.AlignCenter)
        self.layload.addWidget(loadlabl)
        tabImage('menu', 3, self.layload)

        firstrow = QHBoxLayout()
        self.spinlbl,self.spinyear = setYearLbl(firstrow)

        secrow = QHBoxLayout()
        sections = ['calendar', 'race wins', 'driver ranks', 'team ranks']
        self.datalbl,self.combo = setComboBox(1,sections,secrow)

        doubwid, doublay = layinWidget("V")
        doubwid.setObjectName("BlackWid")
        doublay.addLayout(firstrow)
        doublay.addLayout(secrow)

        loadbtn = QPushButton("Load Data in Table")
        loadbtn.setObjectName("Mar")
        loadbtn.clicked.connect(self.race_results)

        self.savelbl = QLabel()
        tabImage('saves', 1, self.savelbl)

        self.savedata = QPushButton("Create SQL Table")
        self.savedata.clicked.connect(self.saving)
        self.mainwid.addWidget(self.savedata)

        changeItems([self.savelbl, self.savedata]).Visibility(False)

        clearlab = QLabel()
        addtoLayload = [doubwid,loadbtn,clearlab,self.savelbl,self.savedata]
        changeItems(addtoLayload).AddingItems(self.layload)
        self.layload.addStretch()


    # extract data from the F1 website and placing it in a table
    def race_results(self):
        self.changer = ""
        if self.sortbool == True:
            changeLay(self.sortlay).clearLay()
            self.sortbool = False
            changeItems([self.sortwid, self.erase,self.eraselbl]).Visibility(False)

        calendar = int(self.spinyear.text())
        datatype = str(self.combo.currentText())

        if datatype == "team ranks" and calendar < 1958:
            QMessageBox.about(self, "Data Error", "No team Competitions before 1958!")
        else:
            changeItems([self.savedata,self.savelbl]).Visibility(True)
            links, var, self.tabheader, cols, numbers = loadingData(datatype)

            for sector in links:
                table = WebScrape(calendar, sector)
                progressload(self.loadtab,10).activate()
                self.content, rows = getRaceData(table,datatype,var,numbers,sector)

            if self.tablemade != False:
                self.tablay.removeWidget(self.tabwid)
            self.makeTable(cols,rows)
            self.tabwid.setObjectName("BlackWid")

            tabImage(datatype.replace(" ", "-"), 2, self.introlbl)
            self.titletext = datatype.title() + " for the " + str(calendar)
            self.titel.setText("List of the " + self.titletext + " Formula 1 Season")

            vertic = []
            for i in range(rows):
                vertic.append(str(i + 1))

            fillTable(self.table, self.content, self.tabheader, vertic)
            tabHeight(self, rows, self.sortbool)
            tabWidth(self,self.table,self.titel,self.scroll,self.tabwid)

        self.goBack()


    # open the SQL menu
    def goBack(self):
        changeLay(self.innerlay).clearLay()
        buttons = backtoSQL(self.innerlay)
        for btn in buttons:
            btn.clicked.connect(self.getList)
        changeLay(self.innerlay).stretchLay()


    # layout for the chosen SQL files category
    def getList(self):
        listname = self.sender().text()
        allcontent = openTab(listname)#.openTab_act()
        changeLay(self.innerlay).clearLay()

        category = str(listname).replace("_", " ").title()
        maintag = QLabel("Category " + category + " Tables")

        maintag.setObjectName("BlackLab")
        maintag.setAlignment(Qt.AlignCenter)
        self.innerlay.addWidget(maintag)
        tabImage('menues', 3, self.innerlay)

        twolinewid, twoinone = layinWidget("H")
        lbltag, self.yearlist = setComboBox(2,allcontent,twoinone)
        twolinewid.setObjectName("RedWid")
        twolinewid.setLayout(twoinone)

        sqlbtn = QPushButton("Load SQL Table")
        sqlbtn.clicked.connect(lambda:self.getSQLtab(allcontent,listname))
        backbtn = QPushButton("Back to Menu")
        backbtn.clicked.connect(self.goBack)
        clearlbl = QLabel()

        addtoInnerLay = [twolinewid,sqlbtn,backbtn,clearlbl,self.eraselbl,self.erase]
        changeItems(addtoInnerLay).AddingItems(self.innerlay)

        changeItems([self.eraselbl, self.erase]).Visibility( False)
        changeLay(self.innerlay).stretchLay()


    # opening a saved SQL file in the table
    def getSQLtab(self,allcontent,listname):

        if self.sortbool != True:
            self.sortbool = True
            changeItems([self.savedata, self.savelbl]).Visibility(False)

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

            changeItems([self.erase,self.eraselbl]).Visibility(True)
            fillTable(self.table, cellsdata, colname, vertic)
            tabWidth(self,self.table,self.titel,self.scroll,self.tabwid)

            if listname!=self.changer:
                self.changer = listname
                changeLay(self.sortlay).clearLay()
                self.SQLsorter(colname)


    # menu for sorting the data in the table
    def SQLsorter(self,colname):
        self.sortwid.setVisible(True)

        if "race" in self.currtab:
            colname.append('order')
        sortlbl, self.sortbox = setComboBox(3, colname, self.sortlay)

        order, self.asc, self.des, sortbtn = sortItems()
        sortbtn.clicked.connect(lambda:self.sorting(colname))

        addtoSortlay = [order, self.asc, self.des, sortbtn]
        changeItems(addtoSortlay).AddingItems(self.sortlay)


    # adjust a new table to the mainwidget
    def makeTable(self,cols,rows):
        self.tablemade = True
        self.table, self.tabwid, self.form, self.scroll = setTable(cols,rows)
        self.tablay.addWidget(self.tabwid)
        tabHeight(self, rows, self.sortbool)


    # input the sorted data in the table
    def sorting(self, colname):
        if 'order' in colname:
            colname.remove('order')

        direct = "DESC"
        if self.asc.isChecked():
            direct = "ASC"

        sorter = self.sortbox.currentText()
        cellsdata,vertic = sortData(self.currtab,sorter,direct)
        fillTable(self.table, cellsdata, colname, vertic)


    # delete a saved SQL file
    def deletion(self):
        ask = eraseTab(self,self.currtab).asktoclear()
        if ask==True:
            self.goBack()
            self.changer=""
            changeLay(self.sortlay).clearLay()


    # save table data as SQL file
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
