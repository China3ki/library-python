import json

from ui.main_not_logged import MainNotLogged
from ui.register import Register


class UiManager:
    def __init__(self):
        self._views = {}
        self._get_view()
        self.states = [MainNotLogged(self._views["mainNotLogged"], self._views["warnings"])]
    def push(self, next_state : str):
        """ Dodaje następny widok do _states, jeśli w _views znajduję podany w argumencie widok. Wyrzuca błąd, jeśli nie znajdzie podanego widoku."""
        if next_state == "back":
            self.pop()
            return
        if next_state == "exit":
            self.clear_states()
            return
        self.states.append(self._get_next_state(next_state))

    def pop(self):
        """ Usuwa ostatni widok ze stosu """
        self.states.pop()
    def clear_states(self):
        """ Czyści stos"""
        self.states.clear()
    def len_states(self) -> int:
        """ Zwraca ilość aktywnych widoków w stosie"""
        return len(self.states)
    def _get_next_state(self, next_state : str):
        match next_state:
            case "mainNotLogged":
                return MainNotLogged(self._views["mainNotLogged"], self._views["warnings"])
            case "login":
                pass
            case "register":
                return Register(self._views["register"], self._views["warnings"])
            case "books":
                pass
            case "settings":
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
