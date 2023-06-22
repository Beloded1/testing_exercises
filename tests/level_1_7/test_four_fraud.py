from functions.level_1_7.four_fraud import find_fraud_expenses
from conftest import make_expenses

def test__find_fraud_expenses__get_no_fraud_expenses_if_have_amount_more_than_max_amount():
    history = [
        make_expenses(amount='5000.00'),
        make_expenses(amount='5001.00'),
        make_expenses(amount='6001.00'),
    ]

    expected_fraud_transactions = []

    fraud_transactions = find_fraud_expenses(history)
    assert fraud_transactions == expected_fraud_transactions


def test__find_fraud_expenses__get_no_fraud_expenses_if_have_len_amount_less_than_min_chain_length():
    history = [
        make_expenses(amount='1000.00'),
        make_expenses(amount='2001.00'),
    ]
    fraud_transactions = find_fraud_expenses(history)
    assert fraud_transactions == []


def test__find_fraud_expenses__if_get_multiple_fraud_chains():
    history = [
        make_expenses(amount='1000.00'),
        make_expenses(amount='1000.00'),
        make_expenses(amount='1000.00'),
        make_expenses(amount='1000.00'),  
    ]
    expected_fraud_transactions = history

    fraud_transactions = find_fraud_expenses(history)
    assert fraud_transactions == expected_fraud_transactions


