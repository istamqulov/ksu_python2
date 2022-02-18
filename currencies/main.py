import requests


def load_currencies():
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    return requests.get(url).json()


print(load_currencies())
