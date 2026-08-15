import psycopg2

from database.connection import get_connection


def is_rate_db(book_id: int, user_id: int) -> tuple[bool, tuple | None]:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT rate FROM book_rates WHERE book_id = %s AND user_id = %s", (book_id, user_id))
                if cur.rowcount > 0:
                    return True, cur.fetchone()[0]
                return False, None

    except (Exception, psycopg2.DatabaseError) as error:
        raise error
def edit_rate_db(book_id: int, user_id: int, new_rate: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE book_rates SET rate = %s WHERE book_id = %s AND user_id = %s", (new_rate, book_id, user_id))
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
def rate_book_db(book_id: int, user_id: int, rate: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO book_rates (book_id, user_id, rate) VALUES (%s, %s, %s)", (book_id, user_id, rate))
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
def remove_rate_db(book_id: int, user_id:int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM book_rates WHERE book_id = %s AND user_id = %s", (book_id, user_id))
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
