import requests

def get_ans(query):
    url = "http://deepprogrammer.pythonanywhere.com/ans/"+str(query)

    response = requests.get(url)

    data = response.json()

    return data['answer']+"."

