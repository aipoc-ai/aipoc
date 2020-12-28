import requests

def get_weather(query):
    url = "http://deepprogrammer.pythonanywhere.com/"+str(query)

    response = requests.get(url)

    data = response.json()

    return data['temperature'],list(data["time"].split("\n"))
