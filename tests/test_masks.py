from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


# Блок masks
def test_get_mask_card_number_many():
    assert get_mask_card_number(["1234567890123456"]) == "1234 56** **** 3456"
    assert get_mask_card_number(["12345678901234567890"]) == "Некорректный номер карты"
    assert get_mask_card_number(["92848927"]) == "Некорректный номер карты"
    assert get_mask_card_number(["928489ds31"]) == "Некорректный номер карты"
    assert get_mask_card_number(["abfjffnjfsnojfno"]) == "Некорректный номер карты"
    assert get_mask_card_number([""]) == "Некорректный номер карты"


def test_get_mask_account():
    assert get_mask_account(["12345678901234567890"]) == "**7890"
    assert get_mask_account(["12345678901234567890123"]) == "Некорректный номер счета"
    assert get_mask_account(["242799"]) == "Некорректный номер счета"
    assert get_mask_account(["оjdsnljknls"]) == "Некорректный номер счета"
    assert get_mask_account([""]) == "Некорректный номер счета"


# Блок widget
def test_mask_account_card():
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"
    assert mask_account_card("Счет") == "Некорректный номер счета"
    assert mask_account_card("Visa 1234567890123456") == "Visa 1234 56** **** 3456"
    assert mask_account_card("Visa") == "Некорректный номер карты"


def test_get_date():
    assert get_date('-1999-10-20rfsff') == '20.10.1999'
    assert get_date('') == 'Некорректная дата'
