import requests
import datetime

URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
CURRENCY_URL = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/%s/currencies/%s.json'


def load_currencies():
    resp = requests.get(URL)
    return resp.json()


def get_currencies_for(currency_code, date: str = "latest"):
    url = CURRENCY_URL % (date, currency_code)
    data = requests.get(url).json()
    return data[currency_code]


def convert_currencies(base_currency, target_currency, amount):
    rates = get_currencies_for(base_currency)
    rate = rates[target_currency]
    return rate * amount


def print_currencies_table_for(currency_code):
    rates = get_currencies_for(currency_code)

    current_time = datetime.datetime.now()
    yesterday = current_time - datetime.timedelta(days=1)
    yesterday_string = yesterday.strftime("%Y-%m-%d")
    previous_rates = get_currencies_for(currency_code, yesterday_string)

    def print_rates_change(currency_code, decimals: int = 2):
        print(
            currency_code,
            round(1 / rates[currency_code], decimals),
            round(1 / (rates[currency_code]) - 1 / previous_rates[currency_code], decimals),
            sep=' | '
        )

    print_rates_change("usd")
    print_rates_change("eur")
    print_rates_change("rub", 3)
    print_rates_change("kzt", 4)
    print_rates_change("uzs", 4)
    print_rates_change("btc")


data = load_currencies()

# for key, value in data.items():
#     print(key.upper(), value)
codes = data.keys()
print(print_currencies_table_for('tjs'))
# print(convert_currencies('usd', 'tjs', 200))

# while True:
#     print("Пожалуйста выберите валюту")
#     user_input = input()
#     user_input = user_input.lower().strip()
#     print(user_input)
#     if user_input in codes:
#         print("Correct")
#         print(get_currencies_for(user_input))
#     else:
#         print("Incorrect")
