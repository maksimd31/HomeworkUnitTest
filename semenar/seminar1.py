# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from math import sqrt
from datetime import datetime
# Задача 0


def square_root(num: float) -> float:
    if num < 0:
        raise RuntimeError(f"Число {num} должно быть неотрицательным")
    return sqrt(num)


def test_square_root_positive():
    assert square_root(25) == 5, "Тест с положительными числами провален"


def test_square_root_zero():
    assert square_root(0) == 0, "Тест с нулевыми значениеями провален"


def test_square_root_negative():
    try:
        square_root(-5)
    except RuntimeError:
        print("Все тесты прошли")


# Задача 4
def happy_NY():
    current_date = datetime.now()
    assert current_date > datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0), "2024 еще не наступил"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_square_root_positive()
    test_square_root_zero()
    test_square_root_negative()

    happy_NY()