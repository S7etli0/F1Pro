def tabHeight(lay, tabrow, check):

    if check==True:
        x = 860
        y = 330
    else:
        x = 470 + (tabrow + 1) * 40
        if x > 850:
            x = 850
            y = 370
        else:
            y = (x - 470)

    lay.setFixedHeight(x)
    lay.table.setFixedHeight(y)
