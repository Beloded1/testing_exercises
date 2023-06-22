from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense
import datetime
import decimal


def test__parse_ineco_expense__succes():
    sms = SmsMessage(
        text="100.00 CARD1234, authcode1234 01.01.23 11:30 Alfa",
        author="Alfa Bank",
        sent_at=datetime.datetime(2023, 1, 1, 11, 30)
    )
    cards = [
        BankCard(last_digits="1234", owner= "Alex"),
        BankCard(last_digits="1234", owner= "Alexandr"),
    ]
    
    result = parse_ineco_expense(sms, cards)
    
    assert result.amount == decimal.Decimal("100.00")
    assert result.card.last_digits == '1234'

