from core.session import Session
from enums.states import States
from services.service_auth import check_account_exist
from ui.state import State
from utils.user_input import user_input_str


class Login(State):
    def __init__(self, view, warnings, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        print(self._view["prompt"])
        success, new_session = self._login_procedure()
        if not success:
            return self._change_state(-1), self.session
        return self._change_state(1), new_session

    def _login_procedure(self):
        """ Przeprowadza procedurę logowania użytkownika, zwraca True i nową sesję"""
        while True:
            email = user_input_str(self._view["email"], self._warnings)
            if email == -1:
                return False, []
            password = user_input_str(self._view["password"], self._warnings)
            if password == -1:
                return False, []
            success, warning, data = check_account_exist(email, password)
            if not success:
                print(self._warnings[warning.value])
                continue
            new_session = Session(data["id"], data["name"],data["surname"],data["birthday"], data["email"],data["is_admin"])
            return True, new_session


    def _change_state(self, user_input) -> States:
        match user_input:
            case -1:
                return States.BACK
            case 1:
                return States.MAIN_LOGGED
            case _:
                raise ValueError("That view does not exist!")