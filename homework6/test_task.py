import pytest

from homework6.task import AverageCalculator


@pytest.fixture
def calculator():
    return AverageCalculator()


def test_calculate_average_empty_list(calculator):
    assert calculator.calculate_average([]) == 0


def test_calculate_average_single_element(calculator):
    assert calculator.calculate_average([5]) == 5


def test_calculate_average_multiple_elements(calculator):
    assert calculator.calculate_average([1, 2, 3, 4, 5]) == 3


def test_compare_averages_first_list_greater(calculator):
    result = calculator.compare_averages([1, 2, 3], [1, 2])
    assert result == "Первый список имеет большее среднее значение"


def test_compare_averages_second_list_greater(calculator):
    result = calculator.compare_averages([1, 2], [1, 2, 3])
    assert result == "Второй список имеет большее среднее значение"


def test_compare_averages_lists_equal(calculator):
    result = calculator.compare_averages([1, 2, 3], [4, 5, 6])
    assert result == "Средние значения равны"


"""
Чтобы запустить тесты и сгенерировать отчет о покрытии кода, выполним следующую команду в терминале:
coverage run --source=./ -m pytest
coverage html
После выполнения команды будет создана папка htmlcov с отчетом о покрытии кода тестами. 
Отчеты хранятся в  файле htmlcov/index.html, чтобы просмотреть отчет в браузере.

Для проверки качества кода с помощью pylint, выполните следующую команду в терминале:
pylint test_task.py
Получившийся отчет о качестве кода будет показан в терминале.

все зависимости в requirements.txt для установки используем $ pip install -r requirements.txt
"""
