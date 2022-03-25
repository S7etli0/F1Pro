from configparser import ConfigParser

def readConfig(file,section):
    parser = ConfigParser()
    parser.read(file)

    data={}
    if parser.has_section(section):
        items = parser.items(section)
        for i in items:
            data[i[0]] = i[1]

        return data