from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import decimal
import datetime
from datetime import datetime


def make_expenses(
    amount: str = "100",
    currency = Currency.RUB,
    card = BankCard(last_digits="1234", owner="Alexandr"),
    spent_in = "Online Store",
    spent_at = datetime(2023, 1, 1, 0, 0, 0),
    category: ExpenseCategory | None = None
) -> Expense:
    return Expense(
        amount=decimal.Decimal(amount),
        currency=currency,
        card=card,
        spent_in=spent_in,
        spent_at=spent_at,
        category=category
    )
