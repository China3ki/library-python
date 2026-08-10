from dataclasses import dataclass
from xmlrpc.client import DateTime


@dataclass
class Book:
    id: int
    name: str
    surname: str
    title: str
    amount: int
    genre: str
    publish_date: DateTime
    avg_rate: float| str