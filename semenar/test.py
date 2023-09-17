# Задание 1. ** В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент
# скидки и возвращает сумму с учетом скидки. Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
# Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения.
#
# *Задание 2. (необязательное) *
# Мы хотим улучшить функциональность нашего интернет-магазина. Ваша задача - добавить два новых метода в класс Shop:
# Метод sortProductsByPrice(), который сортирует список продуктов по стоимости. Метод getMostExpensiveProduct(),
# который возвращает самый дорогой продукт. Напишите тесты, чтобы проверить, что магазин хранит верный список
# продуктов (правильное количество продуктов, верное содержимое корзины).
# Напишите тесты для проверки корректности работы метода getMostExpensiveProduct. Напишите тесты для проверки
# корректности работы метода sortProductsByPrice (проверьте правильность сортировки). Используйте класс
# Product для создания экземпляров продуктов и класс Shop для написания методов сортировки и тестов.
import unittest


class Calculator:
    def calculateDiscount(self, amount: float, discount: float) -> float:
        if not (0 <= discount <= 100):
            raise ArithmeticError("Скидка должна составлять от 0 до 100")
        if amount < 0:
            raise ArithmeticError("Сумма должна быть больше или равна нулю")
        return amount - (amount * discount / 100)


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculateDiscount(self):
        self.assertAlmostEqual(self.calculator.calculateDiscount(100, 10), 90)
        self.assertAlmostEqual(self.calculator.calculateDiscount(200, 15), 170)
        self.assertAlmostEqual(self.calculator.calculateDiscount(300, 20), 240)

    def test_calculateDiscount_with_invalid_amount(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculateDiscount(-100, 10)

    def test_calculateDiscount_with_invalid_discount(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculateDiscount(100, -10)


if __name__ == '__main__':
    unittest.main()
