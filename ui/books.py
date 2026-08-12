from core.session import Session
from enums.books_decision import BooksDecision
from enums.sort_options import SortOptions
from enums.states import States
from services.service_books import ServiceBooks
from ui.state import State
from utils.user_input import user_input_int


class Books(State):
    def __init__(self, view, warnings, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        book_service = ServiceBooks()
        book_service.get_books()


        while True:
            menu = self._build_menu(book_service)
            print(self._view["header"])
            for i, book in enumerate(book_service.books):
                print(
                    f"| {i + 1} | {book.title} | {book.name} {book.surname} | {book.amount} | {book.genre} | {book.publish_date} | {book.avg_rate if book.avg_rate is not None else self._view["noRating"]} |")
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
                self._add_to_favorite(book_service)
                return None
            case BooksDecision.SORT:
                self._sort_procedure(book_service)
                return None
            case BooksDecision.BORROW_BOOK:
                pass
            case BooksDecision.RATE_BOOK:
                self._rate_book_procedure(book_service)
                return None
            case BooksDecision.BACK:
                return BooksDecision.BACK


    def _add_to_favorite(self, book_service):
       """ Rozpoczyna proces dodawania książki do tabeli ulubione  """
       while True:
           user_input = user_input_int(len(book_service.books), self._view["promptAddToFavourite"], self._warnings)
           if user_input == -1:
               return
           success, warning = book_service.add_to_favorite(
               book_service.books[user_input - 1].id, self.session.id)  ## -1, aby odnieść się do prawidłowego indeksu
           if not success:
               print(self._warnings[warning.value])
               continue
           print(f'{self._view["infoAddedToFavorite"]} {book_service.books[user_input - 1].title}')
           return

    def _rate_book_procedure(self, book_service):
        """ Przeprowadza procedurę oceny książki. Jeśli użytkownik już ocenił książkę ma możliwość zmiany dotychczasowej oceny"""
        while True:
            user_input = user_input_int(len(book_service.books), self._view["promptRateBook"], self._warnings)
            if user_input == -1:
                return
            rate_exist, previous_rate = book_service.is_rate(book_service.books[user_input - 1].id, self.session.id)
            if rate_exist:
                success_edit = self._edit_rate_book(book_service, book_service.books[user_input - 1], previous_rate)
                if not success_edit:
                    continue
                return
            success_rate = self._rate_book(book_service, book_service.books[user_input - 1].id)
            if not success_rate:
                continue
            return

    def _rate_book(self, book_service, book_id:int) -> bool:
        """ Pyta użytkownika o ocenę książki. Zwraca True, jeśli, ocena została wystawiona. False, jeśli, nie."""
        user_input_rate = user_input_int(10, self._view["promptRate"], self._warnings)
        if user_input_rate == -1:
            return False
        book_service.rate_book(book_index, self.session.id, user_input_rate)
        print(self._view["infoRateSuccess"])
        return True

    def _edit_rate_book(self, book_service,  book , previous_rate: int) -> bool:
        """ Pozwala na edytowanie poprzedniej oceny książki. Zwraca True, jeśli, ocena została zmieniona. False, jeśli, nie."""
        prompt_edit_rate = self._view["infoEditRate"].replace("[BOOK.TITLE]", book.title).replace("[BOOK.RATE]", str(previous_rate))
        print(prompt_edit_rate)
        user_input = user_input_int(2,self._view["promptEditRate"], self._warnings)
        if user_input == 2 or user_input == -1:
            return False
        user_input_new_rate = user_input_int(10, self._view["promptRate"], self._warnings)
        if user_input_new_rate == -1:
            return False
        book_service.edit_rate(book.id, self.session.id, user_input_new_rate)
        print(self._view["infoEditRateSuccess"])
        return True


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
            return None
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