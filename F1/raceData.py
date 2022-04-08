from F1.teams import TeamContent


# make list to prepare the scraped data for input in the table
def getRaceData(table,data,var,numbers,sector,num = 0):
    content,vertic = [],[]

    for tabrow in table:
        num = str(num+1)
        racelist = tabrow.text.strip().replace("     ", "").split("\n")
        racelist = list(filter(lambda x: x != '', racelist))
        vertic.append(num)

        while len(racelist) < var:
            racelist.append("")
        rowdatas = []

        if data == "team ranks":
            if sector == "drivers":
                numbers = TeamContent(numbers).Drivers(racelist)
            else:
                teaminfo = TeamContent(numbers).Teams(racelist, rowdatas)
                content.append(teaminfo)

        else:
            for cell in numbers:
                rowdatas.append(racelist[cell])
            content.append(rowdatas)
    
    return content, len(content), vertic