# Конвертер валют

## Уровень 1.

Перенести все наши функции 
`load_currencies`
`get_currencies_for`
`convert_currencies`
`compare_currency_rate`
`get_rates_history`

в класс `Currencies`
 
## Уровень 2:
уровень 1 + 

Используя класс Currencies получить даннные по курсу валют за последние 3 дня и сохранить их  в виде CSV.
```
USD  | 2022-02-11  | 2022-02-12 | 2022-02-13 |
USD  |  1          |  1         |  1
TJS  | 11.28       | 11.28      | 11.29
RUB  | 75.6        |  76.64     | 79.4   

```

## Уровень 3
Уровень 2 +

Создать класс APIClient и перенести логику работы с GET и POST запросами в неё

примеры использования
```
client = APIClient(
   base_url="https://cdn.jsdelivr.net"
)

data = client.get(
    path="/gh/fawazahmed0/currency-api@1/latest/currencies.json"
)


```
