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

