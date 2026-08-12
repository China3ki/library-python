from dto.response.response_book import Book
from enums.sort_options import SortOptions
from enums.warnings import Warnings
from repositories.repository_books import get_books_from_db, get_books_row_count, add_to_favorite_db, \
    check_user_favorite_exist, is_rate_db, edit_rate_db, rate_book_db


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
    def add_to_favorite(self, book_id: int, user_id : int) -> tuple:
        """ Waliduję dodawanie polubionej książki do bazy danych"""
        if check_user_favorite_exist(book_id, user_id):
            return False, Warnings.WARNING_BOOK_FAVORITE_EXIST
        add_to_favorite_db(book_id, user_id)
        return True, None

    def is_rate(self, book_id: int, user_id: int) -> tuple[bool, tuple | None]:
        rate_exist, previous_rate = is_rate_db(book_id, user_id)
        return rate_exist, previous_rate

    def edit_rate(self, book_id: int, user_id :int, new_rate: int):
        edit_rate_db(book_id, user_id, new_rate)
        self.get_books()

    def rate_book(self, book_id: int, user_id: int, rate : int):
        rate_book_db(book_id, user_id, rate)
        self.get_books()





