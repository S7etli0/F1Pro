# variables needed for scraping data from the F1 website
def loadingData(data):
    if data == "calendar" or data == "race wins":
        links = ['races']
        var = 8

        if data == 'calendar':
            tabheader = ['country', 'date', 'laps', 'duration']
            numbers = [0, 1, 6, 7]
        else:
            tabheader = ['country', 'first_name', 'last_name', 'nickname', 'team_name']
            numbers = [0, 2, 3, 4, 5]

    elif data == 'driver ranks':
        links = ['drivers']
        var = 7
        tabheader = ['first_name', 'last_name', 'nation', 'team_name', 'points']
        numbers = [1, 2, 4, 5, 6]
    else:
        links = ['drivers', 'team']
        var = 3
        numbers = {}
        tabheader = ['team_name', 'drivers', 'points']

    cols = len(tabheader)

    return links, var, tabheader, cols, numbers