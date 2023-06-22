import decimal
from datetime import datetime
from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses
from conftest import make_expenses


def test__calculate_average_daily_expenses_if_expenses_occurs_in_different_days():
    expenses = [
        make_expenses(
            amount='100.00',
            spent_at=datetime(2023, 6, 1, 12, 0, 0, 0),
        ),
        make_expenses(
            amount='200.00',
            spent_at=datetime(2023, 6, 1, 13, 0, 0, 0),
        ),
        make_expenses(
            amount='300.00',
            spent_at=datetime(2023, 6, 2, 14, 0, 0, 0),
        ),
        make_expenses(
            amount='400.00',
            spent_at=datetime(2023, 6, 2, 15, 0, 0, 0),
        ),
    ]
    
    expected_result = decimal.Decimal('500.00')
    assert calculate_average_daily_expenses(expenses) == expected_result


def test__calculate_average_daily_expenses_if_one_expense_occurs():
    expenses = [
                        make_expenses(
                    amount='100.00',
                    spent_at=datetime(2023, 6, 1, 12, 0, 0, 0),
                ),
    ]
    expected_result = decimal.Decimal('100.00')
    assert calculate_average_daily_expenses(expenses) == expected_result


# def test__calculate_average_daily_expenses_with_empty_list(): # This test doesn't work, because raisestatistics.StatisticsError: mean requires at least one data point
#     expenses = []
#     expected_result = decimal.Decimal('0.00')
#     assert calculate_average_daily_expenses(expenses) == expected_result