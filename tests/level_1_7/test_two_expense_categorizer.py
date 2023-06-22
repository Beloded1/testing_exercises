from functions.level_1_7.two_expense_categorizer import guess_expense_category
from functions.level_1_7.models import ExpenseCategory
import pytest
from conftest import make_expenses


@pytest.mark.parametrize(
    'expense, ExpenseCategory',
    [
        (make_expenses(spent_in='Bastard place'),
        ExpenseCategory.BAR_RESTAURANT),
        (make_expenses(spent_in='nice clean house'),
        ExpenseCategory.SUPERMARKET),
        (make_expenses(spent_in='Netflix USA'),
        ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        (make_expenses(spent_in='Wonder pharm'),
        ExpenseCategory.MEDICINE_PHARMACY),
    ]
)
def test__guess_expense_category_if_spent_in_contains_trigger_words(expense, ExpenseCategory):
    assert guess_expense_category(expense) == ExpenseCategory


@pytest.mark.parametrize(
    'expense, ExpenseCategory',
    [
        (make_expenses(spent_in='Bastard'),
        ExpenseCategory.BAR_RESTAURANT),
        (make_expenses(spent_in='pharm'),
        ExpenseCategory.MEDICINE_PHARMACY),
        (make_expenses(spent_in='www.taxi.yandex.ru'),
        ExpenseCategory.TRANSPORT),

    ]
)
def test__guess_expense_category_if_spent_in_is_trigger_word(expense, ExpenseCategory):
    assert guess_expense_category(expense) == ExpenseCategory


def test__guess_expense_category_if_spent_in_does_not_have_trigger_words(): 
    expense = make_expenses(spent_in='Y Ashota')
    assert guess_expense_category(expense) == None