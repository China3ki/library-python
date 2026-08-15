from enums.loans_decision import LoansDecision
from enums.states import States
from services.service_loans import ServiceLoans
from ui.state import State
from ui.workflows.workflow_favorites import favorite_procedure
from ui.workflows.workflow_rate import rate_book_procedure
from utils.user_input import user_input_int, user_input_str


class MyLoans(State):
    def __init__(self, view, warnings, session, workflow):
        self._workflow = workflow
        super().__init__(view, warnings, session)
    def init_state(self):
        loans_service = ServiceLoans(self.session.id)

        while True:
            loans_service.get_loans(self.session.id)
            if not loans_service.loans:
                print(self._view["infoEmptyLoans"])
                return self._change_state(-1), self.session

            menu = self._build_menu(loans_service)
            print(self._view["header"])
            for i,loan in enumerate(loans_service.loans, start=1):
                print(f"{i} | {loan.title} | {loan.start_date} | {loan.end_date}")
            for i,v in enumerate(menu.values(), start=1):
                print(f"{i} - {v}")
            user_input = user_input_int(len(menu),self._view["prompt"], self._warnings)
            if user_input == -1:
                return self._change_state(-1), self.session
            self._decision(user_input, menu, loans_service)

    def _decision(self, user_input: int, menu: dict[str, str], loans_service : ServiceLoans):
        keys = list(menu.keys())
        match keys[user_input - 1]:
            case LoansDecision.NEXT_PAGE:
                loans_service.page += 1
                loans_service.get_loans(self.session.id)
                return None
            case LoansDecision.PREVIOUS_PAGE:
                loans_service.page -= 1
                loans_service.get_loans(self.session.id)
                return None
            case LoansDecision.SORT:

                return None
            case LoansDecision.RETURN_BOOK:
                return None
            case LoansDecision.RATE_BOOK:
                rate_book_procedure(self.session.id, loans_service.loans, self._workflow, self._warnings)
                return None
            case LoansDecision.ADD_TO_FAVORITE:
                favorite_procedure(self.session.id, loans_service.loans, self._workflow, self._warnings)
                return None
            case LoansDecision.BACK:
                return LoansDecision.BACK
        return None

    def _build_menu(self, loan_service: ServiceLoans) -> dict[str, str]:
        menu = {}
        if loan_service.page > 1:
            menu[LoansDecision.PREVIOUS_PAGE] = self._view[LoansDecision.PREVIOUS_PAGE.value]
        if loan_service.loans > loan_service.loans * loan_service.page:
            menu[LoansDecision.NEXT_PAGE] = self._view[LoansDecision.NEXT_PAGE.value]
        menu[LoansDecision.SORT] = self._view[LoansDecision.SORT.value]
        menu[LoansDecision.RETURN_BOOK] = self._view[LoansDecision.RETURN_BOOK.value]
        menu[LoansDecision.RATE_BOOK] = self._view[LoansDecision.RATE_BOOK.value]
        menu[LoansDecision.ADD_TO_FAVORITE] = self._view[LoansDecision.ADD_TO_FAVORITE.value]
        menu[LoansDecision.BACK] = self._view[LoansDecision.BACK.value]
        return menu

    def _change_state(self, user_input) -> States:
        return States.BACK