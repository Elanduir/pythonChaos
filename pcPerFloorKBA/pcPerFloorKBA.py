import csv

cleanHost = []
cleanUser = []
doc = []
compLoc = {}
with open('resources/Hostnamen.csv') as hostnamenCsv:
    reader = csv.reader(hostnamenCsv, delimiter=',')
    lineCount = 0
    cache = ''
    for row in reader:
        if lineCount != 0:
            if row[0] != '':
                cache = row[0]
            else:
                row[0] = cache
                cleanHost.append(row)
        lineCount += 1
cleanHost.pop()


with open('resources/Benutzer.csv') as benutzerCsv:
    reader = csv.reader(benutzerCsv, delimiter=',')
    lineCount = 0
    cache = ''
    for row in reader:
        if lineCount != 0:
            if row[0] != '':
                cache = row[0]
            else:
                row[0] = cache
                cleanUser.append(row)
        lineCount += 1  
cleanUser.pop()


with open('resources/kbaX_consolidated.csv') as consCsv:
    reader = csv.reader(consCsv, delimiter=',')
    for row in reader:
        compLoc[row[1]] = row

with open('resources/aerzte') as arzt:
    for line in arzt:
        doc.append(line.strip())


class ComputerData:
    def __init__(self):
        self.name = ""
        self.location = ""
        self.userList = []
        self.arztLogin = False

    def __str__(self):
        return "Name: " + self.name + "\nLocation: " + self.location + "\nUserList: " + (", ").join(self.userList) + "\nArztLogin: " + str(self.arztLogin)

compDat = {}
for row in cleanHost:
    if row[0] in compDat:
        compDat[row[0]].userList.append(row[1])
    else:
        cacheComp = ComputerData()
        cacheComp.name = row[0]
        if row[0] in compLoc:
            cacheComp.location = compLoc[row[0]]
        cacheComp.userList.append(row[1])
        compDat[row[0]] = cacheComp

for key in compDat:
    print(compDat[key])
