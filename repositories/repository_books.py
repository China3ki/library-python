from database.connection import get_connection
import psycopg2

def get_books_from_db(limit : int, offset : int, sort_option: str, order_desc: bool):
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

def _modify_query(query: str, sort_option : str, order_desc: bool, limit: int , offset : int ):
    """ Modyfikuję kwerenda według podanych argumentów i decyduje o typie sortu oraz rodzaju. Zwraca zmodyfikowaną kwerenda """
    query += " ORDER BY "
    match sort_option:
        case "id":
            query += "books.id"
        case "name":
            query += "name"
        case "surname":
            query += "surname"
        case "title":
            query += "title"
        case "amount":
            query += "amount"
        case "date":
            query += "publish_date"
        case _:
            query += "books.id"
    if order_desc:
        query += " DESC"
    query += f" LIMIT {limit} OFFSET {offset}"
    return query