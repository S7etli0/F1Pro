# make rows for the list you input with web menu
def getWebList(numbers,data,racelist,rowdatas):

    x, y, name = 0, 0, ""
    if 'race' in data:
        x, y = 2, 3
    elif 'driver' in data:
        x, y = 1, 2

    for cell in numbers:
        if x != 0:
            if cell == x:
                name = racelist[cell] + " "
            elif cell == y:
                name += racelist[cell]
                rowdatas.append(name)
            else:
                rowdatas.append(racelist[cell])
        else:
            rowdatas.append(racelist[cell])

    return rowdatas