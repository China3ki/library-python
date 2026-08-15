from enums.books_decision import BooksDecision
from enums.sort_options import SortOptions
from enums.states import States
from services.service_books import ServiceBooks
from ui.state import State
from utils.user_input import user_input_int
from ui.workflows.workflow_favorites import favorite_procedure
from ui.workflows.workflow_rate import rate_book_procedure


class Books(State):
    def __init__(self, view, warnings, session, workflow):
        self._workflow = workflow
        super().__init__(view, warnings, session)
    def init_state(self):
        book_service = ServiceBooks()
        book_service.get_books()


        while True:
            menu = self._build_menu(book_service)
            print(self._view["header"])
            for i, book in enumerate(book_service.books):
                print(
                    f"| {i + 1} | {book.title} | {book.name} {book.surname} | {book.amount} | {book.genre} | {book.publish_date} | {round(book.avg_rate, 2) if  book.avg_rate is not None else self._view["noRating"]} |")
            for i, v in enumerate(menu.values(), start=1):
                print(f"{i} - {v}")
            user_input = user_input_int(len(menu), self._view["prompt"], self._warnings)
            if user_input == -1:
                return States.BACK, self.session
            decision = self._decision(user_input, menu, book_service)
            if decision == BooksDecision.BACK:
                return States.BACK, self.session


    def _decision(self, user_input: int, menu: dict[BooksDecision, str], book_service) -> BooksDecision | None:
        """ Na podstawie argumentu user_input, decyduję którą opcję następnie wybrać."""
        keys = list(menu.keys())
        match keys[user_input - 1]:
            case BooksDecision.PREVIOUS_PAGE:
                book_service.page -= 1
                book_service.get_books()
                return None
            case BooksDecision.NEXT_PAGE:
                book_service.page += 1
                book_service.get_books()
                return None
            case BooksDecision.ADD_TO_FAVORITE:
                favorite_procedure(self.session.id, book_service.books, self._workflow, self._warnings)
                return None
            case BooksDecision.SORT:
                self._sort_procedure(book_service)
                return None
            case BooksDecision.BORROW_BOOK:
                pass
            case BooksDecision.RATE_BOOK:
                success = rate_book_procedure(self.session.id, book_service.books, self._workflow, self._warnings)
                if success: book_service.get_books()
                return None
            case BooksDecision.BACK:
                return BooksDecision.BACK




    def _sort_procedure(self, book_service):
        """ Na podstawie wprowadzonych danych, wybiera opcję do sortowania."""
        self._print_view("sort_menu")
        user_input = user_input_int(len(self._view["sort_menu"]), self._view["promptSort"], self._warnings)
        match user_input:
            case -1:
                return
            case 1:
                book_service.sort_option = SortOptions.Id
            case 2:
                book_service.sort_option = SortOptions.Name
            case 3:
                book_service.sort_option = SortOptions.Surname
            case 4:
                book_service.sort_option = SortOptions.Title
            case 5:
                book_service.sort_option = SortOptions.Amount
            case 6:
                book_service.sort_option = SortOptions.Date
        sort_order = user_input_int(2, self._view["promptSortDirection"], self._warnings)
        if sort_order == -1:
            return
        if sort_order == 1:
            book_service.order_desc = False
        else:
            book_service.order_desc = True
        book_service.get_books()


    def _build_menu(self, book_service):
        """ Buduje dynamiczne menu, a następnie je zwraca"""
        new_menu = {}
        if book_service.page > 1:
            new_menu[BooksDecision.PREVIOUS_PAGE] = self._view["previousPage"]
        if book_service.books_count > book_service.page * book_service.limit:
            new_menu[BooksDecision.NEXT_PAGE] = self._view["nextPage"]

        if self.session.id is not None:
            new_menu[BooksDecision.ADD_TO_FAVORITE] = self._view["addToFavorite"]
            new_menu[BooksDecision.BORROW_BOOK] = self._view["borrowBook"]
            new_menu[BooksDecision.RATE_BOOK] = self._view["rateBook"]
        new_menu[BooksDecision.SORT] = self._view["sort"]
        new_menu[BooksDecision.BACK] = self._view["back"]
        return new_menu


    def _change_state(self, user_input) -> States:
        return States.BACK