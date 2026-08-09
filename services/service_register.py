from dto.create.dto_user import User
from repositories.service_user import add_new_user
from services.service_auth import verify_user_email, verify_password, compare_password, hash_password
from utils.user_input import user_input_str, user_input_date

def register_procedure(view : dict[str, str], warnings: dict [str,str]):
    """ Przeprowadza procedurę rejestracji. Jeśli użytkownik przerwię, zwraca -1. W innym przypadku zwraca True"""
    print(view["prompt"])
    name = user_input_str(view["name"], warnings)
    if name == -1:
        return False
    surname = user_input_str(view["surname"], warnings)
    if surname == -1:
        return False
    email = verify_user_email(view["email"], warnings)
    if email == -1:
        return False
    birthday = user_input_date(view["birthday"], warnings)
    if birthday == -1:
        return False
    password = verify_password(view["password"], warnings)
    if password == -1:
        return False
    confirmed_password = compare_password(view["password_confirmed"], warnings, password)
    if confirmed_password == -1:
        return False
    new_user = User(name, surname, email, birthday, hash_password(password))
    add_new_user(new_user)
    return True