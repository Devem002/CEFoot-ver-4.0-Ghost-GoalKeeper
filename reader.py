import json
#data = []

with open ("Teams.json", "r") as f:
    data = json.load(f)

print (data['Teams']['teams'][0])
