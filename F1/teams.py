# preparing the race team data for input in the table
class TeamContent():
    def __init__(self, numbers):
        self.numbers = numbers

    # dictionary with the teams and their drivers
    def Drivers(self,racelist):
        if racelist[5] not in self.numbers:
            self.numbers[racelist[5]] = str(racelist[1]) + " " + str(racelist[2])
        else:
            # elif str(numbers[racelist[5]]).count('&') =< 3:
            self.numbers[racelist[5]] += " & " + str(racelist[1]) + " " + str(racelist[2])
        return self.numbers

    # add teams data and data from the dictionary
    def Teams(self,racelist,rowdatas):
        rowdatas.append(racelist[1])
        if racelist[1] in self.numbers:
            rowdatas.append(self.numbers[str(racelist[1])])
        else:
            rowdatas.append("")
        rowdatas.append(racelist[2])
        return rowdatas