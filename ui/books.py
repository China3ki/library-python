from services.service_books import ServiceBooks
from ui.state import State
from utils.user_input import user_input_str, user_input_int


class Books(State):
    def __init__(self, view, warnings, session):
        super().__init__(view, warnings, session)
    def init_state(self):
        book_service = ServiceBooks()
        book_service.get_books("id", False)


        while True:
            menu = self._build_menu(book_service)
            print(self._view["header"])
            for i, book in enumerate(book_service.books):
                print(
                    f"| {i + 1} | {book.title} | {book.name} {book.surname} | {book.amount} | {book.genre} | {book.publish_date} | {book.avg_rate} |")
            for i, v in enumerate(menu.values(), start=1):
                print(f"{i} - {v}")
            user_input = user_input_int(len(menu), self._view["prompt"], self._warnings)





    def _build_menu(self, book_service):
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
        if self._session.id is None:
            match user_input:
                case 1:
                    pass
                case 2:
                    pass
        else:
            match user_input:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4: pass
        pass