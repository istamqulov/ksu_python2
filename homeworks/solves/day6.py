"""
# День 6. Повторение пройденных тем

## Уровень 1

1. Создать функцию get_volume которая в качестве аргумента получает сторону куба и возвращает его обьем
2. Создать Программу для печати таблицы умножения

## Уровень 2

Все что в уровне 1
Плюс
1. Написать функцию is_prime которая будет возращать значение True или False в зависимости от того является ли число простым или нет.
2. Напечатать все простые числа до 10 000

## Уровень 3
Все что в уровне 2
Плюс
1. Записать в файл все простые числа до 1 000 000

"""


def get_volume(a):
    return a**3


def print_multiples():
    max_n = 10
    for i in range(2, max_n+1):
        for j in range(2, max_n+1):
            print(i, "x", j, "=", i*j)
        print()


def is_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_primes(max_n=10_000):
    for i in range(1, max_n):
        if is_prime(i):
            print(i)


def eratosthenes(n):
    sieve = list(range(n + 1))
    # [0, 1, 2, 3, ....]
    for i in sieve:
        if i > 1:
            for j in range(2*i, n + 1, i):
                sieve[j] = 0

    return sieve


def test():
    assert get_volume(5) == 125
    print_multiples()
    assert is_prime(7)
    print_primes(10_000_000)


print(eratosthenes(10000000))
