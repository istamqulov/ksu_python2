from typing import Optional, Iterable

import requests
import datetime
import csv



def get(url, ):
    resp = requests.get(url)
    return resp.json()


class Currencies(object):
    CURRENCIES_URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
    CURRENCY_URL = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/%s/currencies/%s.json'

    def load_currencies(self):
        return get(self.CURRENCIES_URL)

    def get_currencies_for(self, currency_code, date: str = "latest"):
        url = self.CURRENCY_URL % (date, currency_code)
        data = get(url)
        return data[currency_code]

    def convert_currencies(self, base_currency, target_currency, amount):
        rates = self.get_currencies_for(base_currency)
        rate = rates[target_currency]
        return rate * amount

    def compare_currency_rate(self, base_currency, target_currency, start_date, end_date):
        start_rate = self.get_currencies_for(base_currency, start_date)
        end_rate = self.get_currencies_for(base_currency, end_date)
        return end_rate[target_currency] - start_rate[target_currency]

    def get_rates_history(self, base_currency, target_currency, days=10):
        current_time = datetime.datetime.now()
        results = {}

        for day in range(days):
            day_time = current_time - datetime.timedelta(days=day)
            date_string = day_time.strftime("%Y-%m-%d")
            rates = self.get_currencies_for(base_currency, date_string if day else 'latest')
            results[date_string] = rates[target_currency]

        return results


def print_currencies_table_for(currency_code):
    currencies = Currencies()
    rates = currencies.get_currencies_for(currency_code)

    current_time = datetime.datetime.now()
    yesterday = current_time - datetime.timedelta(days=1)
    yesterday_string = yesterday.strftime("%Y-%m-%d")
    previous_rates = currencies.get_currencies_for(currency_code, yesterday_string)

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


def export_csv(base_currency: str, days: int = 3, target_currencies: list = None):  # Optional[Iterable]
    current_time = datetime.datetime.now()
    currencies = Currencies()

    # Будет хранить данные в словаре в следующем формате
    """
        {
            "2022-02-28": {
                 "usd": 11.28
            }
        }
    """
    results = {}

    if target_currencies is None:
        # Если валюты не указаны получить все валюты и использовать их
        target_currencies = list(currencies.load_currencies().keys())

    for day in range(days):
        # итерация по дням
        day_time = current_time - datetime.timedelta(days=day)
        date_string = day_time.strftime("%Y-%m-%d")
        rates = currencies.get_currencies_for(base_currency, date_string if day else 'latest')

        results[date_string] = {}

        for currency in target_currencies:
            # вставка данных  в наш results
            results[date_string][currency] = rates[currency]

    # добавляем базовую валюту в название файла чтобы исключить конфликты
    with open('export_rates_%s.csv' % base_currency, 'w') as csv_file:

        writer = csv.writer(csv_file)

        # записываем первую строку
        dates = list(results.keys())
        writer.writerow(
            [base_currency, ] + dates
        )
        for currency in target_currencies:
            row = [currency]

            for date in dates:
                row.append(results[date][currency])
            writer.writerow(row)


export_csv('rub', days=5)
#
# currencies = Currencies()
#
# print(currencies.compare_currency_rate("rub", "tjs", "2022-02-11", "2022-02-26"))
# print(currencies.get_rates_history("rub", "tjs", days=10))
# data = currencies.load_currencies()
#
# # for key, value in data.items():
# #     print(key.upper(), value)
# # codes = data.keys()
# # print(print_currencies_table_for('rub'))
