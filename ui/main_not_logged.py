from ui.state import State
from utils.user_input import user_input_int


class MainNotLogged(State):
    def __init__(self, view : dict, warnings :dict, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        self._print_view()
        user_input = user_input_int(len(self._view["menu"]), self._view["prompt"], self._warnings)
        return self._change_state(user_input), self._session
    def _change_state(self, user_input : int | None) -> str:
        match user_input:
            case -1:
                return "back"
            case 1:
                return "login"
            case 2:
                return "register"
            case 3:
                return "books"
            case 4:
                return "settings"
            case 5:
                return "exit"
            case _:
                raise ValueError("That view does not exist!")