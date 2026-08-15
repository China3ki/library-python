from services.service_rates import is_rate, rate_book, remove_rate, edit_rate
from utils.user_input import user_input_int


def rate_book_procedure(user_id:int, books : list, workflow: dict[str, str], warnings: dict[str, str])-> bool:
    """ Przeprowadza procedurę oceny książki. Jeśli użytkownik już ocenił książkę ma możliwość zmiany dotychczasowej oceny"""
    while True:
        user_input = user_input_int(len(books), workflow["promptRateBook"], warnings)
        if user_input == -1:
            return False
        rate_exist, previous_rate = is_rate(books[user_input - 1].id, user_id)
        if rate_exist:
            success_decision = _decision_rate_book(user_id, books[user_input - 1], workflow, warnings, previous_rate)
            if not success_decision:
                continue
            break
        success_rate = _rate_book(books[user_input - 1].id, user_id, workflow, warnings)
        if not success_rate:
            continue
        break
    return True

def _rate_book(book_id: int, user_id: int, workflow: dict[str, str], warnings: dict[str,str]) -> bool:
    """ Pyta użytkownika o ocenę książki. Zwraca True, jeśli, ocena została wystawiona. False, jeśli, nie."""
    user_input_rate = user_input_int(10, workflow["promptRate"], warnings)
    if user_input_rate == -1:
        return False
    rate_book(book_id, user_id, user_input_rate)
    print(workflow["infoRateSuccess"])
    return True


def _decision_rate_book(user_id: int, book, workflow: dict[str, str], warnings: dict[str,str],  previous_rate: int) -> bool:
    """ Pozwala na edytowanie poprzedniej oceny książki lub usunąć. Zwraca True, jeśli, ocena została zmieniona. False,
    jeśli, nie."""
    prompt_edit_rate = workflow["infoEditRate"].replace("[BOOK.TITLE]", book.title).replace("[BOOK.RATE]",
                                                                                              str(previous_rate))
    print(prompt_edit_rate)
    user_input = user_input_int(3, workflow["promptEditRate"], warnings)
    if user_input == 3 or user_input == -1:
        return False
    if user_input == 2:
        remove_rate(book.id, user_id)
        print(workflow["infoRemoveRate"])
        return True
    user_input_new_rate = user_input_int(10, workflow["promptRate"], warnings)
    if user_input_new_rate == -1:
        return False
    edit_rate(book.id, user_id, user_input_new_rate)
    print(workflow["infoEditRateSuccess"])
    return True