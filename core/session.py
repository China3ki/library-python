from dataclasses import dataclass
from xmlrpc.client import DateTime


@dataclass
class Session:
    id:int | None
    name:str | None
    surname:str | None
    birthday: str | DateTime
    email: str | None
    is_admin: bool | None
