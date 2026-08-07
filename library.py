from utils.ui_manager import UiManager


class Library:
    def __init__(self):
        self._ui_manager = UiManager()

    def app(self):
        while self._ui_manager.len_states():
            pass

a = Library()
a.app()