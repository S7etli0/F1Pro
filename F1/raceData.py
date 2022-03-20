from F1.teams import TeamContent


def getRaceData(table,data,var,numbers,sector):
    content = []

    for tabrow in table:
        racelist = tabrow.text.strip().replace("     ", "").split("\n")
        racelist = list(filter(lambda x: x != '', racelist))

        while len(racelist) < var:
            racelist.append("")
        rowdatas = []

        if data == "team ranks":
            teaminfo = TeamContent(sector, numbers, racelist, rowdatas)
            content.append(teaminfo)

        else:
            for cell in numbers:
                rowdatas.append(racelist[cell])
            content.append(rowdatas)
    
    return content