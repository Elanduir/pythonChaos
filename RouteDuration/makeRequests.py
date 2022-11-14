import requests

json = []
file = open("./requests.txt")
for line in file:
    response = requests.get(line)
    json.append(response.text)

print(json)
