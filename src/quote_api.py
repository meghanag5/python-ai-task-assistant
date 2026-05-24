import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    print(response)
    data = response.json()
    print(data)

get_quote()