from abc import ABC, abstractmethod

from enums.states import States


class State(ABC):
    def __init__(self, view, warnings, session):
        self._view = view
        self._warnings = warnings
        self.session = session
    @abstractmethod
    def init_state(self):
        pass
    @abstractmethod
    def _change_state(self, user_input) -> States:
        pass
    def _print_view(self, menu : str = "menu"):
        for i, view in enumerate(self._view[menu]):
            print(f" {i + 1} - {view}")
