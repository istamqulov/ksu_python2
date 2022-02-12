import math


def convert_displacement(displacement_string: str) -> float:
    """
    :param displacement_string: "2993 ccm"
    :return: 3.0
    """
    displacement, _ = displacement_string.split()
    displacement = float(displacement) / 1000

    return math.ceil(displacement * 10) / 10


def split_text_into_words(text: str) -> list:
    """
    :param text: "My name is Zohirjon"
    :return:  ["My", "name", "is", "Zohirjon"]
    """

    return text.split()


def merge_words(words: list) -> str:
    """
    :param words: ["My", "name", "is", "Zohirjon"]
    :return: "My name is Zohirjon"
    """
    return " ".join(words)


def get_triangle_square(a: float, b: float, c: float) -> float:
    """
    :param a: 5
    :param b: 4
    :param c: 3
    :return: 6
    """
    p = (a + b + c) / 2
    return math.sqrt(
        p * (p-a) * (p-b) * (p-c)
    )


def get_fuel_consumption(consumption_string: str) -> float:
    """
    :param consumption_string: "6,3 l/100km"
    :return: 6.3
    """
    consumption = consumption_string.split()[0]
    consumption = consumption.replace(",", ".")
    return float(consumption)


def test():
    assert convert_displacement("2993 ccm") == 3.0
    assert convert_displacement("2637 ccm") == 2.7

    assert len(split_text_into_words("My name is Zohirjon")) == 4
    assert len(split_text_into_words("")) == 0
    assert merge_words(["Hello", "world!"]) == "Hello world!"

    assert get_triangle_square(5, 4, 3) == 6

    assert get_fuel_consumption("6,3 l/100km") == 6.3

test()




