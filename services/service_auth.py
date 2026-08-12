from enum import Enum
from typing import Any

import bcrypt

from enums.warnings import Warnings
from repositories.repository_user import email_not_exist, login
from utils.validation import validate_email, validate_password




def verify_user_email(email : str) -> tuple[bool, Warnings | None]:
    """ Weryfikuje od użytkownika czy email jest prawidłowy, a następnie sprawdza, czy email już istnieje w bazie danych"""
    if not validate_email(email):
        return False, Warnings.WARNING_EMAIL_REGEX
    if not email_not_exist(email):
        return False, Warnings.WARNING_UNIQUE_EMAIL
    return True, None

def verify_password(password: str) -> tuple[bool, Warnings | None]:
    """ Weryfikuje od użytkownika czy hasło spełnia wymagania """
    if not validate_password(password):
        return False, Warnings.WARNING_PASSWORD_REQUIREMENTS
    return True, None


def compare_password(password : str, confirmed_password : str) -> tuple[bool, Warnings] | tuple[bool, None]:
    """ Weryfikuje czy hasła są takie same """
    if password != confirmed_password:
        return False, Warnings.WARNING_COMPARE_PASSWORDS
    return True, None
def check_account_exist(email : str, password: str) -> tuple[bool, Warnings, None] | tuple[bool, None, Any]:
    """ Weryfikuje czy konto istnieje, jeśli tak, zwraca dane użytkownika i True. Jeśli nie zwraca pustą krotkę oraz False"""
    success, data = login(email)
    if not success:
        return False, Warnings.WARNING_WRONG_LOGIN_DATA, None
    compare_passwords = check_password(password, data["password"])
    if not compare_passwords:
        return False, Warnings.WARNING_WRONG_LOGIN_DATA, None
    return True, None, data



def hash_password(plain_text_password):
    """ Koduję hasło, następnie zwraca zakodowane."""
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())
def check_password(plain_text_password, hashed_password):
    """ Porównuje hasło wpisane przez użytkownika z hasłem w bazie danych"""
    return bcrypt.checkpw(plain_text_password, hashed_password)