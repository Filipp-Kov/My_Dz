from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(str_number_card_or_account: str, number_account: list, number_card: list) -> str:
    """Обрабатывает информацию о картах и о счетах"""

    if "Счет" in str_number_card_or_account or "счет" in str_number_card_or_account:  # используем маскировку счета
        number_account = list(str_number_card_or_account[-20:])
        get_mask_account(number_account)
        number_account_mask = get_mask_account(number_account)
        text = str(f"{list(str_number_card_or_account[:-21])} {number_account_mask}")

    else:  # используем маскировку карты
        number_card = list(str_number_card_or_account[-16:])
        get_mask_card_number(number_card)
        number_card_mask = get_mask_card_number(number_card)
        text = str(f"{list(str_number_card_or_account[:-17])} {number_card_mask}")

    return text


def get_date(str_date: str) -> str:
    """Принимает строку с датой и возвращает дату в формате "ДД.ММ.ГГГГ" """

    str_date = list(str_date)
    tru_date = str(f"'{str_date[9:11]}.{str_date[6:8]}.{str_date[1:5]}'")

    return tru_date
