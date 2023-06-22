import decimal
from datetime import datetime, timedelta
from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses
from statistics import StatisticsError
import pytest


def test__calculate_average_daily_expenses_if_expenses_occurs_in_different_days(make_expense):
    day = datetime(2023, 6, 1, 0, 0, 0)
    expenses = [
        make_expense(amount='100.00', spent_at=day,),
        make_expense(amount='200.00', spent_at=day + timedelta(hours=1),),
        make_expense(amount='300.00', spent_at=day + timedelta(days=1)),
        make_expense(amount='400.00', spent_at=day + timedelta(days=1, hours=1),),
    ]
    
    expected_result = decimal.Decimal('500.00')
    assert calculate_average_daily_expenses(expenses) == expected_result


def test__calculate_average_daily_expenses_if_one_expense_occurs(make_expense):
    day = datetime(2023, 6, 1, 0, 0, 0)
    expenses = [
                    make_expense(amount='100.00', spent_at=day,),
    ]
    expected_result = decimal.Decimal('100.00')
    assert calculate_average_daily_expenses(expenses) == expected_result


def test__calculate_average_daily_expenses_with_empty_list():
    expenses = []
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses(expenses)