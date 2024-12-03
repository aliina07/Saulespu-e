import requests

def info():

    lapa = requests.get("https://vvsprogramm.github.io/A/")
    print(lapa.text)
    return lapa.text