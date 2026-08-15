import datetime

from repositories.repository_books import is_available_db
from repositories.repository_loans import is_loan_db, loan_book_db
from services.service_books import decrease_book_amount


def loan_book(book_id:int, user_id:int):
    start_date = datetime.datetime.now().date()
    end_date = start_date + datetime.timedelta(days=7)
    loan_book_db(book_id, user_id, start_date, end_date)
    decrease_book_amount(book_id)

def is_loan(book_id: int, user_id: int):
    return is_loan_db(book_id, user_id)
def is_available(book_id: int) -> bool:
    amount =  is_available_db(book_id)
    if amount > 0: return True
    return False