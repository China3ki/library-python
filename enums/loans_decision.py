from enum import Enum


class LoansDecision(Enum):
    NEXT_PAGE = "nextPage"
    PREVIOUS_PAGE = "previousPage"
    SORT = "sort"
    RETURN_BOOK = "returnBook"
    RATE_BOOK = "rateBook"
    ADD_TO_FAVORITE = "addToFavorite"
    BACK = "back"
    