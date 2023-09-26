from book_repository import BookRepository
from homework4.book import Book


class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def get_books(self):
        return self.book_repository.get_books()

    def add_book(self, title, author):
        book = Book(title, author)
        self.book_repository.save_book(book)
