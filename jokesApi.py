import requests


def joke():
    URL = 'https://v2.jokeapi.dev/joke/Any'
    jokes = requests.get(url=URL)
    data = jokes.json()
    joke = ""
    if data["type"] == "twopart":
        setup = data["setup"]
        delivery = data["delivery"]
        joke = setup + "\n" + delivery
    else:
        joke = data["joke"]

    return joke
