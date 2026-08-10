from dto.create.dto_user import User
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
            return self._change_state(1), self._session
        return self._change_state(-1), self._session

    def register_procedure(self):
        """ Przeprowadza procedurę rejestracji. Jeśli użytkownik przerwię, zwraca -1. W innym przypadku zwraca True"""
        print(self._view["prompt"])
        name = user_input_str(self._view["name"], self._warnings)
        if name == -1:
            return False
        surname = user_input_str(self._view["surname"], self._warnings)
        if surname == -1:
            return False
        email = verify_user_email(self._view["email"], self._warnings)
        if email == -1:
            return False
        birthday = user_input_date(self._view["birthday"], self._warnings)
        if birthday == -1:
            return False
        password = verify_password(self._view["password"], self._warnings)
        if password == -1:
            return False
        confirmed_password = compare_password(self._view["password_confirmed"], self._warnings, password)
        if confirmed_password == -1:
            return False
        new_user = User(name, surname, email, birthday, hash_password(password))
        add_new_user(new_user)
        return True

    def _change_state(self, user_input) -> str:
        match user_input:
            case -1:
                return "back"
            case 1:
                print(self._view["register_completed_successfully"])
                return "back"
            case _:
                raise ValueError("That view does not exist!")