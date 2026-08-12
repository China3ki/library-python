from enums.states import States
from ui.state import State
from utils.user_input import user_input_str, user_input_int


class MainLogged(State):
    def __init__(self, view, warnings, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        print(self._view["welcomePrompt"] + f"{self.session.name}!")
        self._print_view()
        user_input = user_input_int(len(self._view["menu"]), self._view["prompt"],self._warnings)
        return self._change_state(user_input), self.session
    def _change_state(self, user_input) -> States:
        match user_input:
            case 1:
                return States.BOOKS
            case _:
                raise ValueError("That view does not exist!")
