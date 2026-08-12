import json

from core.session import Session
from enums.states import States
from ui.books import Books
from ui.login import Login
from ui.main_logged import MainLogged
from ui.main_not_logged import MainNotLogged
from ui.register import Register


class UiManager:
    def __init__(self):
        self._views = {}
        self._get_view()
        self.states = [MainNotLogged(self._views["mainNotLogged"], self._views["warnings"], Session(None, None, None, None, None, None))]
    def push(self, next_state : States, session):
        """ Dodaje następny widok do _states, jeśli w _views znajduję podany w argumencie widok. Wyrzuca błąd, jeśli nie znajdzie podanego widoku."""
        if next_state == States.BACK:
            self.pop(session)
            return
        if next_state == States.EXIT:
            self.clear_states()
            return
        self.states.append(self._get_next_state(next_state, session))

    def pop(self, session):
        """ Usuwa ostatni widok ze stosu """
        self.states.pop()
        if len(self.states) > 0:
            self.states[-1].session = session

    def clear_states(self):
        """ Czyści stos"""
        self.states.clear()
    def len_states(self) -> int:
        """ Zwraca ilość aktywnych widoków w stosie"""
        return len(self.states)
    def _get_next_state(self, next_state : States, session):
        match next_state:
            case States.MAIN_LOGGED:
                self.clear_states() # Czyści stack po zalogowaniu
                return MainLogged(self._views["mainLogged"], self._views["warnings"], session)
            case States.MAIN_NOT_LOGGED:
                return MainNotLogged(self._views["mainNotLogged"], self._views["warnings"], session)
            case States.LOGIN:
                return Login(self._views["login"], self._views["warnings"], session)
            case States.REGISTER:
                return Register(self._views["register"], self._views["warnings"], session)
            case States.BOOKS:
                return Books(self._views["books"], self._views["warnings"], session)
            case States.SETTINGS:
                pass
            case _: raise ValueError("That view does not exist!")

    def _get_view(self):
        """ Ustawia język programu na podstawię configu w folderze głównym"""
        lang = ""
        with open("settings.json", "r", encoding="utf-8") as f:
            lang = json.load(f)["lang"]
        match lang:
            case "pl":
                with open("languages/pl.json", "r", encoding="utf-8") as f:
                    self._views = json.load(f)
            case "en":
                pass
                # with open("languages/en.json", "r", encoding="utf-8") as f:
                #     self._views = json.load(f)
