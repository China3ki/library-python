from dto.response.response_book import Book
from repositories.repository_books import get_books_from_db, get_books_row_count


class ServiceBooks:
    def __init__(self):
        self.page = 1
        self.limit = 10
        self.books_count = get_books_row_count()
        self.books = []
    def get_books(self, sort_option: str, order_desc: bool):
        """ Tworzy paginację, pobiera książki z bazy danych i twórzy obiekty książki"""
        offset = (self.page * self.limit) - self.limit if self.page > 1 else 0
        books = get_books_from_db(self.limit, offset, sort_option, order_desc)
        for book in books:
            new_book = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7] if book[7] is not None else "Brak ocen")
            self.books.append(new_book)
