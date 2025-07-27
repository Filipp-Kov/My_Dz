from src.widget import mask_account_card, get_date


# Модуль widget
def test_mask_account_card():
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"
    assert mask_account_card("Счет") == "Некорректный номер счета"
    assert mask_account_card("Visa 1234567890123456") == "Visa 1234 56** **** 3456"
    assert mask_account_card("Visa") == "Некорректный номер карты"


def test_get_date():
    assert get_date("-1999-10-20rfsff") == "20.10.1999"
    assert get_date("") == None
