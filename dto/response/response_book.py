from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    id: int
    name: str
    surname: str
    title: str
    amount: int
    genre: str
    publish_date: datetime
    avg_rate: float | None