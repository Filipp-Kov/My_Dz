import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture()
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# Модуль filter_by_currency
def test_filter_by_currency_filtering(transactions):
    filtered_transactions = filter_by_currency(transactions, "USD")
    result = list(filtered_transactions)
    assert len(result) == 3

    filtered_transactions = filter_by_currency(transactions, "RUB")
    result = list(filtered_transactions)
    assert len(result) == 2

    filtered_transactions = filter_by_currency(transactions, "EUR")
    result = list(filtered_transactions)
    assert len(result) == 0

    filtered_transactions = filter_by_currency(transactions, "")
    result = list(filtered_transactions)
    assert len(result) == 0


# Модуль transaction_descriptions
def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))

    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]

    assert descriptions == expected


# Модуль card_number_generator
def test_card_number_generator():
    test_1 = list(card_number_generator(1, 5))
    assert test_1 == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    test_2 = card_number_generator(1234567812345678, 1234567812345678)
    assert next(test_2) == "1234 5678 1234 5678"
