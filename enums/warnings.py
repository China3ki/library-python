from enum import Enum


class Warnings (Enum):
    WARNING_EMAIL_REGEX = "warningEmailRegex"
    WARNING_UNIQUE_EMAIL = "warningUniqueEmail"
    WARNING_PASSWORD_REQUIREMENTS = "warningPasswordRequirements"
    WARNING_COMPARE_PASSWORDS = "warningComparePasswords"
    WARNING_WRONG_LOGIN_DATA = "warningWrongLoginData"

    WARNING_BOOK_AMOUNT = "warningBookAmount"
    WARNING_BOOK_FAVORITE_EXIST = 'warningBookFavoriteExist'