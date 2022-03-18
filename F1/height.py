def tabHeight(lay,tabrow):

    x = 470 + (tabrow + 1) * 40
    if x > 850:
        lay.setFixedHeight(850)
        lay.table.setFixedHeight(375)

    else:
        lay.setFixedHeight(x)
        lay.table.setFixedHeight(x - 470)
