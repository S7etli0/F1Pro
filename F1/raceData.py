from F1.teams import TeamContent


# make list to prepare the scraped data for input in the table
def getRaceData(table,data,var,numbers,sector):
    content = []

    for tabrow in table:
        racelist = tabrow.text.strip().replace("     ", "").split("\n")
        racelist = list(filter(lambda x: x != '', racelist))

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
    
    return content, len(content)