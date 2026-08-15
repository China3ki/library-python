import datetime

from dto.response.response_loan import Loan
from enums.sort_options_loans import SortOptionsLoans
from repositories.repository_books import is_available_db
from repositories.repository_loans import is_loan_db, loan_book_db, get_loans_row_count, get_loans_db
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
class ServiceLoans:
    def __init__(self, user_id):
        self.page = 1
        self.limit = 10
        self.loans_count = get_loans_row_count(user_id)
        self.sort_option = SortOptionsLoans.TITLE
        self.sort_order_desc = False
        self.loans = []
    def get_loans(self, user_id):
        offset = (self.page * self.limit) - self.limit if self.page > 1 else 0
        loans = get_loans_db(user_id, self.sort_option, self.sort_order_desc, self.limit, offset)
        self.loans.clear()
        if loans:
          for loan in loans:
              self.loans.append(Loan(loan[0], loan[1], loan[2], loan[3]))



