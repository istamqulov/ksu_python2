import requests

URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"


def load_currencies():
    resp = requests.get(URL)
    return resp.json()

data = load_currencies()

for key, value in data.items():
    print(key, value)
