def tabHeight(lay, tabrow, check):

    if check==True:
        lay.setFixedHeight(860)
        lay.table.setFixedHeight(330)
    else:
        x = 470 + (tabrow + 1) * 40
        if x > 850:
            lay.setFixedHeight(850)
            lay.table.setFixedHeight(370)
        else:
            lay.setFixedHeight(x)
            lay.table.setFixedHeight(x - 470)

