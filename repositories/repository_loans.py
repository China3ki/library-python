import psycopg2

from database.connection import get_connection

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
