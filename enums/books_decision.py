from enum import Enum


class BooksDecision(Enum):
    PREVIOUS_PAGE = "previousPage"
    NEXT_PAGE = "nextPage"
    SORT = "sort"
    ADD_TO_FAVORITE ="addToFavorite"
    BORROW_BOOK = "borrowBook"
    RATE_BOOK = "rateBook"
    BACK = "back"