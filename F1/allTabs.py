from F1.mySQL import startSQL

# collect the names of all sql tables in the chosen category

# class openTab():
#     def __init__(self,name):
#         self.name = name
#
#
#     def openTab_act(self):
#         name = self.name

def openTab(category):
        mydb, curs = startSQL(True)
        curs.execute("SHOW TABLES")

        allcontent = []
        for x in curs:
            titel = str(x)[2:-3]

            if category in titel:
                z = len(titel)
                allcontent.append(titel[z-4:z])

        return allcontent
