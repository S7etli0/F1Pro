# variables needed for scraping data from the F1 website
def loadingData(data):

    if data == "calendar" or data == "race wins":
        links = ['races']
        var = 8

        if data == 'calendar':
            tabheader = ['country', 'full_date', 'race_laps', 'duration']
            numbers = [0, 1, 6, 7]
        else:
            tabheader = ['country', 'full_name', 'nickname', 'team_name']
            numbers = [0, 2, 3, 4, 5]

    elif data == 'driver ranks':
        links = ['drivers']
        var = 7
        tabheader = ['full_name', 'nation', 'team_name', 'all_points']
        numbers = [1, 2, 4, 5, 6]

    else:
        links = ['drivers', 'team']
        var = 3
        numbers = {}
        tabheader = ['team_name', 'full_drivers_list', 'all_points']

    cols = len(tabheader)

    return links, var, tabheader, cols, numbers