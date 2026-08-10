from dto.response.response_book import Book
from services.service_books import ServiceBooks
from ui.state import State
from utils.user_input import user_input_str, user_input_int


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
                return "back", self._session
            decision = self._decision(user_input, menu, book_service)
            if decision == "back":
                return "back", self._session


    def _decision(self, user_input: int, menu: dict[str, str], book_service) -> str | None:
        """ Na podstawie argumentu user_input, decyduję którą opcję następnie wybrać."""
        keys = list(menu.keys())
        match keys[user_input - 1]:
            case "previousPage":
                book_service.page -= 1
                book_service.get_books()
                return None
            case "nextPage":
                book_service.page += 1
                book_service.get_books()
                return None
            case "sort":
                self._sort_procedure(book_service)
            case "borrowBook":
                pass
            case "rateBook":
                pass
            case "back":
                return "back"


    def _sort_procedure(self, book_service):
        """ Na podstawie wprowadzonych danych, wybiera opcję do sortowania."""
        self._print_view("sort_menu")
        user_input = user_input_int(len(self._view["sort_menu"]), self._view["prompt_sort"], self._warnings)
        match user_input:
            case -1:
                return
            case 1:
                book_service.sort_option = "id"
            case 2:
                book_service.sort_option = "name"
            case 3:
                book_service.sort_option = "surname"
            case 4:
                book_service.sort_option = "title"
            case 5:
                book_service.sort_option = "amount"
            case 6:
                book_service.sort_option = "date"
        sort_order = user_input_int(2, self._view["prompt_sort_direction"], self._warnings)
        if sort_order == 1:
            book_service.order_desc = False
        else:
            book_service.order_desc = True
        book_service.get_books()


    def _build_menu(self, book_service):
        """ Buduje dynamiczne menu, a następnie je zwraca"""
        new_menu = {}
        if book_service.page > 1:
            new_menu["previousPage"] = self._view["previousPage"]
        if book_service.books_count > book_service.page * book_service.limit:
            new_menu["nextPage"] = self._view["nextPage"]

        if self._session.id is not None:
            new_menu["borrowBook"] = self._view["borrowBook"]
            new_menu["rateBook"] = self._view["rateBook"]
        new_menu["sort"] = self._view["sort"]
        new_menu["back"] = self._view["back"]
        return new_menu


    def _change_state(self, user_input) -> str:
        return "back"