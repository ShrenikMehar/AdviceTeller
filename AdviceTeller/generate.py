import requests

url = "https://api.adviceslip.com/advice"

def randomadvice(x):
    if(x==0):
        Data = requests.get(url)
        json_data = Data.json()
        random_advice = json_data["slip"]
        return (random_advice["advice"])