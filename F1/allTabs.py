from F1.mySQL import startSQL

# class openTab():
#     def __init__(self,name):
#         self.name = name
#
#
#     def openTab_act(self):
#         name = self.name

def openTab(name):
        mydb, curs = startSQL(True)
        curs.execute("SHOW TABLES")

        allcontent = []
        for x in curs:
            titel = str(x)[2:-3]

            if name in titel:
                z = len(titel)
                allcontent.append(titel[z-4:z])

        return allcontent
