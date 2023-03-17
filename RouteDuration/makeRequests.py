import requests

json = []
file = open("./requests14.txt")
for line in file:
    response = requests.get(line)
    json.append(response.text)

print(json)
