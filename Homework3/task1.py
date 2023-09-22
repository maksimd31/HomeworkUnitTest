import unittest

"""
*Задание 1.
Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, 
является ли переданное число четным или нечетным. (код приложен в презентации)
"""

def evenOddNumber(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


class TestEvenOddNumber(unittest.TestCase):
    def test_even_number(self):
        result = evenOddNumber(4)
        self.assertEqual(result, "Even")

    def test_odd_number(self):
        result = evenOddNumber(7)
        self.assertEqual(result, "Odd")

    def test_zero(self):
        result = evenOddNumber(0)
        self.assertEqual(result, "Even")

    def test_negative_even_number(self):
        result = evenOddNumber(-6)
        self.assertEqual(result, "Even")

    def test_negative_odd_number(self):
        result = evenOddNumber(-9)
        self.assertEqual(result, "Odd")


if __name__ == '__main__':
    unittest.main()
