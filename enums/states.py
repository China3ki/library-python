from enum import Enum


class States(Enum):
    MAIN_NOT_LOGGED = "mainNotLogged"
    MAIN_LOGGED = "mainLogged"
    MY_LOANS = "myLoans"
    BOOKS = "books"
    REGISTER = "register"
    LOGIN = "login"
    SETTINGS = "settings"
    BACK = "back"
    EXIT = "exit"