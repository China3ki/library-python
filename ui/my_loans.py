from enums.states import States
from ui.state import State


class MyLoans(State):
    def __init__(self, view, warnings, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        pass
    def _change_state(self, user_input) -> States:
        return