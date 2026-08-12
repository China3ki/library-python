from database.connection import get_connection
import psycopg2

from enums.sort_options import SortOptions


def get_books_from_db(limit : int, offset : int, sort_option: SortOptions, order_desc: bool):
    """ Pobiera książki z bazy danych, i filtruję po wskazanym przez użytkownika opcjach"""
    query = "SELECT books.id, authors.name AS name, authors.surname AS surname, books.title, books.amount, genres.name AS genre, books.publish_date, AVG(book_rates.rate) AS avg_rate FROM books INNER JOIN authors ON books.author_id = authors.id INNER JOIN genres ON books.genre_id = genres.id LEFT JOIN book_rates ON book_rates.book_id = books.id GROUP BY books.id, authors.name, authors.surname, books.title, books.amount, genres.name, books.publish_date"
    query = _modify_query(query, sort_option, order_desc, limit, offset)
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
def get_books_row_count() -> int:
    """ Zwraca ilość książek w tabeli books"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(id) FROM books")
                return  cur.fetchone()[0]
    except (Exception, psycopg2.DatabaseError) as error:
        raise error

def _modify_query(query: str, sort_option : SortOptions, order_desc: bool, limit: int , offset : int ):
    """ Modyfikuję kwerenda według podanych argumentów i decyduje o typie sortu oraz rodzaju. Zwraca zmodyfikowaną kwerenda """
    query += " ORDER BY "
    match sort_option:
        case SortOptions.Id:
            query += "books.id"
        case SortOptions.Name:
            query += "name"
        case SortOptions.Surname:
            query += "surname"
        case SortOptions.Title:
            query += "title"
        case SortOptions.Amount:
            query += "amount"
        case SortOptions.Date:
            query += "publish_date"
        case _:
            query += "books.id"
    if order_desc:
        query += " DESC"
    query += f" LIMIT {limit} OFFSET {offset}"
    return query

def add_to_favorite_db(book_id : int, user_id: int):
    """ Przyjmuję id książki oraz id użytkownika, a następnie dodaje do tabeli ulubione"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO favorites (book_id, user_id) VALUES(%s, %s)", (book_id, user_id))
    except (Exception,  psycopg2.DatabaseError) as error:
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