import requests

URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
CURRENCY_URL = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/%s.json'


def load_currencies():
    resp = requests.get(URL)
    return resp.json()


def get_currencies_for(currency_code):
    url = CURRENCY_URL % currency_code
    data = requests.get(url).json()
    return data[currency_code]


def convert_currencies(base_currency, target_currency, amount):
    rates = get_currencies_for(base_currency)
    rate = rates[target_currency]
    return rate * amount

data = load_currencies()

for key, value in data.items():
    print(key.upper(), value)
codes = data.keys()
print(convert_currencies('usd', 'tjs', 0.5))

while True:
    print("Пожалуйста выберите валюту")
    user_input = input()
    user_input = user_input.lower().strip()
    print(user_input)
    if user_input in codes:
        print("Correct")
        print(get_currencies_for(user_input))
    else:
        print("Incorrect")
