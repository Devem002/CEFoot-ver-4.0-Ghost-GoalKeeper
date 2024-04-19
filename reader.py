import json


def readData():
    with open ("Teams.json", "r") as f:
        data = json.load(f)
        return data

