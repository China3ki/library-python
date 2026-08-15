from repositories.repository_favorites import check_user_favorite_exist, add_to_favorite_db, remove_favorite_db


def is_favorite(book_id: int, user_id: int) -> bool:
    """ Zwraca True, jeśli w bazie znajduje się polubiona książka. False, jeśli nie"""
    return check_user_favorite_exist(book_id, user_id)

def add_to_favorite(book_id: int, user_id: int):
    """ Dodaje polubioną książkę do bazy danych"""
    add_to_favorite_db(book_id, user_id)
def remove_favorite(book_id:int, user_id: int):
    remove_favorite_db(book_id, user_id)