from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import decimal
import datetime
from datetime import datetime
import pytest


@pytest.fixture
def make_expense():
    def inner(
        amount: str | None = None,
        card: BankCard | None = None,
        spent_in: str | None = None,
        spent_at: datetime | None = None,
        category: ExpenseCategory | None = None,
    ) -> Expense:
        amount = amount or "100"
        return Expense(
            amount=decimal.Decimal(amount),
            currency=Currency.RUB,
            card=card or BankCard(last_digits="1234", owner="Alexandr"),
            spent_in=spent_in or "Online Store",
            spent_at=spent_at or datetime(2023, 1, 1, 0, 0, 0),
            category=category or ExpenseCategory.TRANSPORT,
        )

    return inner