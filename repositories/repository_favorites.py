import psycopg2

from database.connection import get_connection


def add_to_favorite_db(book_id : int, user_id: int):
    """ Przyjmuję id książki oraz id użytkownika, a następnie dodaje do tabeli ulubione"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO favorites (book_id, user_id) VALUES(%s, %s)", (book_id, user_id))
    except (Exception,  psycopg2.DatabaseError) as error:
        raise error
def remove_favorite_db(book_id : int, user_id: int):
    """ Usuwa książkę z tabeli ulubione"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM favorites WHERE book_id = %s AND user_id = %s", (book_id, user_id))
    except (Exception, psycopg2.DatabaseError) as error:
        raise error


def check_user_favorite_exist(book_id :int, user_id :int) -> bool:
    """ Weryfikuję czy użytkownik nie ma już dodanej książki do ulubionych"""
    try:
        with get_connection() as coon:
            with coon.cursor() as cur:
                cur.execute("SELECT user_id FROM favorites WHERE book_id = %s AND user_id = %s", (book_id, user_id))
                if cur.rowcount > 0:
                    return True
                return False
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
