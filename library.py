from utils.ui_manager import UiManager


class Library:
    def __init__(self):
        self._ui_manager = UiManager()

    def app(self):
        while self._ui_manager.len_states():
            self._ui_manager.push(self._ui_manager.states[-1].init_state())



a = Library()
a.app()