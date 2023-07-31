import csv
import re
from os import walk

# ComputerData class declaration to store all info
class ComputerData:
    def __init__(self):
        self.name = ""
        self.ci = ""
        self.location = ""
        self.model = ""
        self.status = ""
        self.mac1 = ""
        self.mac2 = ""
        self.userList = []

    def convertUserlist(self):
        uList = []
        for u in self.userList:
            uList.append((", ").join(u))
        return ("\n").join(uList)

    def __iter__(self):
        return iter([self.name, self.ci, self.location, self.model, self.status, self.mac1, self.mac2, self.convertUserlist()])

    def __str__(self):
        return str(self.name) + "\n" + str(self.ci) + "\n" + str(self.model) + "\n" + str(self.location) +"\n" + str(self.status) + "\n" + str(self.mac1) + "\n" + str(self.mac2) + "\n" + str(self.userList)


def userFilter(compList, userList):
    result = [];
    for comp in compList:
        for uC in comp.userList:
            if uC[0] in userList:
                result.append(comp)
    return result

def writeCompCSV(fileLoc, compList):
    with open(fileLoc, "w") as csv_output:
        wr = csv.writer(csv_output, delimiter= ';')
        wr.writerow(["Hostname", "CI", "Location", "Model", "Status", "Mac1", "Mac2", "Users"])
        for comp in compList:
            wr.writerow(list(comp))
    
migPath = 'resources/migData'
cleanHost = []
cleanUser = []
doc = []
compLoc = {}
compDat = {}
user0802 = []
user0803 = []
comp0802 = []

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

for row in cleanHost:
    match = re.search("(?<=\()[a-zA-Z0-9]+(?=\))", row[1])
    if match:
        user = match.group()
    else:
        user = "no user found"
    if row[0] in compDat:
        compDat[row[0]].userList.append([user, row[2]])
    else:
        cacheComp = ComputerData()
        cacheComp.name = row[0]
        if cacheComp.name in compLoc:
            cacheComp.ci = compLoc[cacheComp.name][0]
            cacheComp.model = compLoc[cacheComp.name][5]
            cacheComp.location = compLoc[cacheComp.name][14]
            cacheComp.status = compLoc[cacheComp.name][9]
            cacheComp.mac1 = compLoc[cacheComp.name][15]
            cacheComp.mac2 = compLoc[cacheComp.name][17]
        cacheComp.userList.append([user, row[2]])
        compDat[row[0]] = cacheComp


for (dirpath, dirnames, filenames) in walk(migPath):
    for fileN in filenames:
        filePath = dirpath + "/" + fileN
        reqUser = []
        with open(filePath) as inputFile:
            for line in inputFile:
                reqUser.append(line.strip())
        compReq = userFilter(compDat.values(), reqUser)
        writeCompCSV("output/" + fileN + ".csv", compReq)
            
