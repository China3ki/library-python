from dto.response.response_book import Book
from enums.sort_options import SortOptions
from repositories.repository_books import get_books_row_count, get_books_from_db


class ServiceBooks:
    def __init__(self):
        self.page = 1
        self.limit = 10
        self.books_count = get_books_row_count()
        self.sort_option = SortOptions.Id
        self.order_desc = False
        self.books = []
    def get_books(self):
        """ Tworzy paginację, pobiera książki z bazy danych i twórzy obiekty książki"""
        offset = (self.page * self.limit) - self.limit if self.page > 1 else 0
        books = get_books_from_db(self.limit, offset, self.sort_option, self.order_desc)
        self.books.clear()
        for book in books:
            new_book = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7])
            self.books.append(new_book)






