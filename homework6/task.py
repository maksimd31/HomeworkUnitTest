from typing import List


class AverageCalculator:
    def calculate_average(self, numbers: List[int]) -> float:
        """Рассчитывает среднее значение списка чисел."""
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def compare_averages(self, list1: List[int], list2: List[int]) -> str:
        """Сравнивает средние значения двух списков и возвращает соответствующее сообщение."""
        average1 = self.calculate_average(list1)
        average2 = self.calculate_average(list2)

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average1 < average2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


"""
Создаем класс AverageCalculator в соответствии с принципами объектно-ориентированного программирования. 
В классе будут определены методы для расчета среднего значения списка и сравнения средних значений двух списков. 
Также напишем тесты с использованием Pytest для проверки правильности работы программы и генерации отчета о 
покрытии кода тестами. Наконец, проверим качество кода с помощью pylint.
"""