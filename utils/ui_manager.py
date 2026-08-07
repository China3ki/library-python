class UiManager:
    def __init__(self):
        self._states = ["a", "b", "a", "D"]
        self._views= ["not_logged", "logged", "admin_logged"]
    def push(self, next_state : str):
        """ Dodaje następny widok do _states, jeśli w _views znajduję podany w argumencie widok. Wyrzuca błąd, jeśli nie znajdzie podanego widoku."""
        for view in self._views:
            if view == next_state:
                self._states.append(view)
                return
        raise ValueError("That view does not exist!")

    def pop(self):
        """ Usuwa ostatni widok ze stosu """
        self._states.pop()
    def clear_states(self):
        """ Czyści stos"""
        self._states.clear()
    def len_states(self) -> int:
        """ Zwraca ilość aktywnych widoków w stosie"""
        return len(self._states)

