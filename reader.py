import json

#funcion para leer la data de un json y retornarla en forma de biblioteca
def readData():
    with open ("Teams.json", "r") as f:
        data = json.load(f)
        return data

