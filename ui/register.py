from services.service_register import register_procedure
from ui.state import State

class Register(State):
    def __init__(self, view, warnings):
        super().__init__(view, warnings)

    def init_state(self) -> str:
        completed_procedure = register_procedure(self._view, self._warnings)
        if completed_procedure:
            self._change_state(1)
        self._change_state(-1)

    def _change_state(self, user_input) -> str:
        match user_input:
            case -1:
                return "back"
            case 1:
                return "mainViewLogged"
            case _:
                raise ValueError("That view does not exist!")