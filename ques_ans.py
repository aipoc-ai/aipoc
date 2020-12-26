import urllib, json

def get_ans(query):
    url = "http://deepprogrammer.pythonanywhere.com/ans/"+str(query)

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    print(data)

get_ans("what is gold")