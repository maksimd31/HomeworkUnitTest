import unittest

"""
Задание 2.
Разработайте и протестируйте метод numberInInterval, который проверяет, 
попадает ли переданное число в интервал (25;100). (код приложен в презентации)
"""

def numberInInterval(num):
    if 25 < num < 100:
        return True
    else:
        return False


class TestNumberInInterval(unittest.TestCase):
    def test_number_in_interval(self):
        result = numberInInterval(50)
        self.assertTrue(result)

    def test_number_less_than_25(self):
        result = numberInInterval(10)
        self.assertFalse(result)

    def test_number_greater_than_100(self):
        result = numberInInterval(150)
        self.assertFalse(result)

    def test_number_equal_to_25(self):
        result = numberInInterval(25)
        self.assertFalse(result)

    def test_number_equal_to_100(self):
        result = numberInInterval(100)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
