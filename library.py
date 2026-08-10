import bcrypt

from utils.ui_manager import UiManager


class Library:
    def __init__(self):
        self._ui_manager = UiManager()

    def app(self):
        while self._ui_manager.len_states():
            next_view, session = self._ui_manager.states[-1].init_state()

            self._ui_manager.push(next_view, session)



a = Library()
a.app()
