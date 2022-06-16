import json
import os

directory  = "walking"
for file in os.listdir(directory):
    name = os.path.join(directory, file)
    with open(name, "r") as openfile:
        jsonObj = json.load(openfile)

    elements = jsonObj["rows"][0]["elements"]
    print(file)
    for e in elements:
        print(e["duration"]["value"])



