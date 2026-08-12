from dto.create.dto_user import User
from enums.states import States
from enums.warnings import Warnings
from repositories.repository_user import add_new_user
from services.service_auth import verify_user_email, verify_password, compare_password, hash_password
from utils.user_input import user_input_str, user_input_date


from ui.state import State

class Register(State):
    def __init__(self, view, warnings, session):
        super().__init__(view, warnings, session)

    def init_state(self):
        completed_procedure = self.register_procedure()
        if completed_procedure:
            return self._change_state(1), self.session
        return self._change_state(-1), self.session



    def register_procedure(self):
        """ Przeprowadza procedurę rejestracji. Jeśli użytkownik przerwię, zwraca -1. W innym przypadku zwraca True"""
        print(self._view["prompt"])
        name = user_input_str(self._view["name"], self._warnings)
        if name == -1:
            return False
        surname = user_input_str(self._view["surname"], self._warnings)
        if surname == -1:
            return False

        email = ""
        while True:
            user_input_email = user_input_str(self._view["email"], self._warnings)
            if user_input_email == -1:
                return False
            success, warning = verify_user_email(user_input_email)
            if not success:
                print(self._warnings[warning.value])
                continue
            email = user_input_email
            break

        birthday = user_input_date(self._view["birthday"], self._warnings)
        if birthday == -1:
            return False

        password = ""
        print(self._view["passwordInfo"])
        while True:
            user_input_password = user_input_str(self._view["password"], self._warnings)
            if user_input_password == -1:
                return False
            success, warning = verify_password(user_input_password)
            if not success:
                print(self._warnings[warning.value])
                continue
            password = user_input_password
            break

        while True:
            user_input_confirmed_password = user_input_str(self._view["passwordConfirmed"], self._warnings)
            if user_input_confirmed_password == -1:
                return False
            success, warning = compare_password(password, user_input_confirmed_password)
            if not success:
                print(self._warnings[warning.value])
                continue
            break

        new_user = User(name, surname, email, birthday, hash_password(password))
        add_new_user(new_user)
        return True

    def _change_state(self, user_input) -> States:
        match user_input:
            case -1:
                return States.BACK
            case 1:
                print(self._view["registerCompletedSuccessfully"])
                return States.BACK
            case _:
                raise ValueError("That view does not exist!")