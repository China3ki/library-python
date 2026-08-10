from ui.state import State
from utils.user_input import user_input_str


class MainLogged(State):
    def __init__(self, view, warnings, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        print(self._view["welcomePrompt"] + f"{self._session.name}!")
        self._print_view()
        user_input = user_input_str(self._view["prompt"], self._warnings)
        pass
    def _change_state(self, user_input) -> str:
        pass