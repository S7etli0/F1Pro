# preparing the race team data for input in the table
class TeamContent():
    def __init__(self, numbers):
        self.numbers = numbers

    # dictionary with the teams and their drivers
    def Drivers(self,racelist):
        check = racelist[5]

        if check not in self.numbers:
            self.numbers[check] = str(racelist[1]) + " " + str(racelist[2])
        elif len(self.numbers[check].split('&'))<3:
            self.numbers[check] += " & " + str(racelist[1]) + " " + str(racelist[2])

        return self.numbers

    # add teams data and data from the dictionary
    def Teams(self,racelist,rowdatas):
        check = racelist[1]
        rowdatas.append(check)

        if check in self.numbers:
            drivers = (self.numbers[str(check)]).split(" & ")
            while len(drivers) != 3:
                drivers.append("None")

            for i in range(len(drivers)):
                rowdatas.append(drivers[i])
        else:
            for i in range(3):
                rowdatas.append("None")

        rowdatas.append(racelist[2])

        return rowdatas