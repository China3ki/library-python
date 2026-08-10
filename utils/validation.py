import re
def validate_email(email: str) -> bool:
    """ Waliduje email i zwraca True, jeśli, email jest prawidłowy"""
    pattern = "[^@]+@[^@]+\\.[^@]+"
    if re.search(pattern, email):
        return True
    return False
def validate_password(password : str) -> bool:
    """ Waliduję hasło, jeśli spełnia wymagania zwraca True"""
    number_pattern = re.search("[0-9]", password)
    uppercase_letter = re.search("[A-Z]", password)
    special_character = re.search("(?=.*?[#?!@$%^&*-])", password)
    password_length = len(password) >= 8
    if number_pattern and uppercase_letter and special_character and password_length:
        return True
    return False