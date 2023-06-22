from functions.level_1_7.three_is_subscription import is_subscription
from datetime import datetime


def test__is_subscription__no_subscription_when_expense_occurs_in_same_month(make_expense):
    expense = make_expense(spent_in='Megafon', spent_at=datetime(2023, 3, 2, 0, 0))
    history = [
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 1, 1, 0, 0)),
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 1, 3, 0, 0)),
        make_expense(spent_in='Alfa Bank', spent_at=datetime(2023, 2, 3, 0, 0)),
    ]
    assert is_subscription(expense, history) == False 


def test__is_subscription__when_successful_subscription_with_three_months_in_history_and_one_expense_was_in_each_month(make_expense):
    expense = make_expense(spent_in='Megafon', spent_at=datetime(2023, 6, 1, 0, 0))
    history = [
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 1, 1, 0, 0)),
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 2, 1, 0, 0)),
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 3, 1, 0, 0)),
    ]
    assert is_subscription(expense, history) == True 


def test__is_subscription__when_no_subscription_with_two_months_in_history_and_one_expense_in_each_month(make_expense):
    expense = make_expense(spent_in='Megafon', spent_at=datetime(2023, 6, 1, 0, 0))
    history = [
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 1, 1, 0, 0)),
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 2, 1, 0, 0)),
    ]
    assert is_subscription(expense, history) == False


def test__is_subscription__when_no_subscription_with_three_months_in_history_and_few_expenses_in_some_month(make_expense):
    expense = make_expense(spent_in='Megafon', spent_at=datetime(2023, 3, 2, 0, 0))
    history = [
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 1, 1, 0, 0)),
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 2, 1, 0, 0)),
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 2, 2, 0, 0)),
        make_expense(spent_in='Megafon', spent_at=datetime(2023, 3, 1, 0, 0)),
    ]
    assert is_subscription(expense, history) == False