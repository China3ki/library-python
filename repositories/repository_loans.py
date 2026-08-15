import psycopg2

from database.connection import get_connection
from enums.sort_options_loans import SortOptionsLoans


def loan_book_db(book_id: int, user_id:int, start_date, end_date):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO loans VALUES (%s, %s, %s, %s) ", (user_id, book_id, start_date, end_date))
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def is_loan_db(book_id: int, user_id:int) -> bool:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id FROM loans WHERE book_id = %s AND user_id = %s", (book_id, user_id))
                if cur.rowcount > 0:
                    return True
                return False
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
def get_loans_row_count(user_id: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id FROM loans WHERE user_id = %s", (user_id,))
                return cur.rowcount
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
def get_loans_db(user_id: int, sort_option : SortOptionsLoans, order_desc: bool, limit: int , offset : int ):
    """ Pobiera wypożyczenia z bazy danych i zwraca """
    query = "SELECT books.id, books.title, start_date, end_date FROM loans INNER JOIN books ON books.id = book_id WHERE user_id = %s "
    query = _modify_query(query, sort_option, order_desc, limit, offset)
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (user_id,))
                return cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def _modify_query(query: str, sort_option : SortOptionsLoans, order_desc: bool, limit: int , offset : int  ):
    query += "ORDER BY "
    match sort_option:
        case SortOptionsLoans.TITLE:
            query += "books.title"
        case SortOptionsLoans.START_DATE:
            query += "start_date"
        case SortOptionsLoans.END_DATE:
            query += "end_date"
        case _:
            query += "books.title"
    if order_desc:
        query += " desc"
    query += f" limit {limit} OFFSET {offset}"
    return query

