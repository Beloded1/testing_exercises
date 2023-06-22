from functions.level_1_7.two_expense_categorizer import guess_expense_category
from functions.level_1_7.models import ExpenseCategory
import pytest


@pytest.mark.parametrize(
    'spent_in, expected_category',
    [
        ('Bastard place', ExpenseCategory.BAR_RESTAURANT),
        ('nice clean house', ExpenseCategory.SUPERMARKET),
        ('Netflix USA', ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        ('Wonder pharm', ExpenseCategory.MEDICINE_PHARMACY),
    ]
)
def test__guess_expense_category_if_spent_in_contains_trigger_words(spent_in, expected_category, make_expense):
    expense = make_expense(spent_in=spent_in)
    assert guess_expense_category(expense) == expected_category


@pytest.mark.parametrize(
    'spent_in, expected_category',
    [
        ('Bastard', ExpenseCategory.BAR_RESTAURANT),
        ('pharm', ExpenseCategory.MEDICINE_PHARMACY),
        ('www.taxi.yandex.ru', ExpenseCategory.TRANSPORT),

    ]
)
def test__guess_expense_category_if_spent_in_is_trigger_word(spent_in, expected_category, make_expense):
    expanse = make_expense(spent_in=spent_in)
    assert guess_expense_category(expanse) == expected_category


def test__guess_expense_category_if_spent_in_does_not_have_trigger_words(make_expense): 
    expense = make_expense(spent_in='Y Ashota')
    assert guess_expense_category(expense) == None