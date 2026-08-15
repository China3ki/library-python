from datetime import datetime
from dataclasses import dataclass


@dataclass
class Loan:
    id: int
    title: str
    start_date: datetime
    end_date: datetime