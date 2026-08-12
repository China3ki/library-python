from enums.states import States
from ui.state import State
from utils.user_input import user_input_int


class MainNotLogged(State):
    def __init__(self, view : dict, warnings :dict, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        self._print_view()
        user_input = user_input_int(len(self._view["menu"]), self._view["prompt"], self._warnings)
        return self._change_state(user_input), self.session
    def _change_state(self, user_input : int | None) -> States:
        match user_input:
            case -1:
                return States.BACK
            case 1:
                return States.LOGIN
            case 2:
                return States.REGISTER
            case 3:
                return States.BOOKS
            case 4:
                return States.SETTINGS
            case 5:
                return States.EXIT
            case _:
                raise ValueError("That view does not exist!")