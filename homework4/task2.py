from unittest import TestCase
from unittest.mock import Mock
from book_service import BookService
from book_repository import BookRepository
from book import Book


class BookServiceTest(TestCase):
    def test_get_books(self):
        # Создаем мок-объект BookRepository
        book_repository = Mock(spec=BookRepository)

        # Создаем список книг, которые мы ожидаем получить от репозитория
        expected_books = [
            Book(title="Book 1", author="Author 1"),
            Book(title="Book 2", author="Author 2"),
            Book(title="Book 3", author="Author 3"),
        ]

        # Устанавливаем ожидаемое поведение мок-объекта
        book_repository.get_books.return_value = expected_books

        # Создаем экземпляр BookService и передаем ему мок-объект BookRepository
        book_service = BookService(book_repository)

        # Вызываем метод get_books у экземпляра BookService
        actual_books = book_service.get_books()

        # Проверяем, что полученный результат совпадает с ожидаемым
        self.assertEqual(actual_books, expected_books)
