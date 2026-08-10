import psycopg2
from database.connection import get_connection


def email_not_exist(email : str) -> bool:
    """ Weryfikuje, czy email istnieje w bazie danych. Jeśli nie, zwraca True w innym przypadku zwraca False"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT email FROM users WHERE email = %s LIMIT 1", (email,))
                row_count = cur.rowcount
                if row_count == 0:
                    return True
                return False
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
def add_new_user(user) -> bool:
    """ Dodaje użytkownika do bazy danych"""
    query = "INSERT INTO users (name, surname, email, birthday, password, is_admin) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (user.name, user.surname, user.email, user.birthday, user.password, False)
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                conn.commit()
                return True
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def login(email: str):
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT id, name, surname, birthday,  email, password, is_admin from users WHERE email = %s", (email,))
                if cur.rowcount == 0:
                    return False, ()
                db_data = cur.fetchone()
                user_data = {"id": db_data[0], "name": db_data[1], "surname": db_data[2], "birthday": db_data[3], "email": db_data[4], "password": db_data[5], "is_admin": db_data[6] }
                return True, user_data
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
