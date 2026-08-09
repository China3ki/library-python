import bcrypt

from repositories.service_user import email_not_exist
from utils.user_input import user_input_str
from utils.validation import validate_email, validate_password


def verify_user_email(prompt : str, warnings : dict[str, str]) -> str | int:
    """ Weryfikuje od użytkownika czy email jest prawidłowy, a następnie sprawdza, czy email już istnieje w bazie danych"""
    while True:
        user_input = user_input_str(prompt, warnings)
        if user_input == -1:
            return user_input
        if not validate_email(user_input):
            print(warnings["warningEmailRegex"])
            continue
        unique_email = email_not_exist(user_input)
        if not unique_email:
            print(warnings["warningUniqueEmail"])
            continue
        return user_input
def verify_password(prompt :str, warnings: dict[str, str]) -> str | int:
    """ Weryfikuje od użytkownika czy hasło spełnia wymagania """
    while True:
        user_input = user_input_str(prompt, warnings)
        if user_input == -1:
            return user_input
        if not validate_password(user_input):
            print(warnings["warningPasswordRequirements"])
            continue
        return user_input

def compare_password(prompt : str, warnings: dict[str, str], password : str) -> bool | int:
    """ Weryfikuje czy hasła są takie same """
    while True:
        user_input = user_input_str(prompt, warnings)
        if user_input == 1:
            return user_input
        if user_input != password:
            print(warnings["warningComparePasswords"])
            continue
        return True
def hash_password(plain_text_password):
    """ Koduję hasło, następnie zwraca zakodowane."""
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())
def check_password(plain_text_password, hashed_password):
    """ Porównuje hasło wpisane przez użytkownika z hasłem w bazie danych"""
    return bcrypt.checkpw(plain_text_password, hashed_password)