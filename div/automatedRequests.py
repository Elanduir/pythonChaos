import json
import requests
file = open("church12/driving.txt")
lines = file.readlines()
for line in lines:
        x = requests.get(line)
        y = json.loads(x.text)
        n = y["origin_addresses"][0] + ".json"
        with open("driving12/" + n, "w") as outfile:
            json.dump(y, outfile)
