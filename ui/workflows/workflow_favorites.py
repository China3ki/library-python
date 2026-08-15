from services.service_favorites import is_favorite, remove_favorite, add_to_favorite
from utils.user_input import user_input_int

def favorite_procedure(user_id: int, books: list, workflow: dict[str, str], warnings : dict[str, str]):
    """ Rozpoczyna proces dodawania książki do tabeli ulubione  """
    while True:
        user_input = user_input_int(len(books), workflow["promptAddToFavourite"], warnings)
        if user_input == -1:
            return
        if is_favorite(books[user_input - 1].id, user_id):
            print(workflow["infoFavorite"])
            favorite_decision = user_input_int(2, workflow["promptFavoriteDecision"], warnings)
            if favorite_decision == -1 or favorite_decision == 2:
                return
            remove_favorite(books[user_input - 1].id, user_id)
            return

        add_to_favorite(
            books[user_input - 1].id, user_id)  ## -1, aby odnieść się do prawidłowego indeksu
        print(f'{workflow["infoAddedToFavorite"]} {books[user_input - 1].title}')
        return