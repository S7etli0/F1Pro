# change the title of the table widget
def sqlTitel(currtab):
    mytitle = currtab.split("_")

    if len(mytitle) > 2:
        category = str(mytitle[0] + " " + mytitle[1]).title()
        theYear = str(mytitle[2])
    else:
        category = str(mytitle[0]).title()
        theYear = str(mytitle[1])

    titletext = "List of the " + category + " for the " + theYear + " Formula 1 Season"

    return titletext