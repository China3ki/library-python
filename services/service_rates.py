from repositories.repository_rates import is_rate_db, edit_rate_db, rate_book_db, remove_rate_db


def is_rate(book_id: int, user_id: int) -> tuple[bool, tuple | None]:
    rate_exist, previous_rate = is_rate_db(book_id, user_id)
    return rate_exist, previous_rate


def edit_rate(book_id: int, user_id: int, new_rate: int):
    edit_rate_db(book_id, user_id, new_rate)


def rate_book(book_id: int, user_id: int, rate: int):
    rate_book_db(book_id, user_id, rate)

def remove_rate(book_id: int, user_id: int):
    remove_rate_db(book_id, user_id)