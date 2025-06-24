from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(str_number_card_or_account: str) -> str:
    """Обрабатывает информацию о картах и о счетах"""

    if "счет" in str_number_card_or_account.lower():  # используем маскировку счета
        number_account = list(str_number_card_or_account[-20:])
        number_account_mask = get_mask_account(number_account)
        word = str_number_card_or_account[:-21]
        if number_account_mask == "Некорректный номер счета":
            text = "Некорректный номер счета"
        else:
            text = str(f"{word.title()} {number_account_mask}")

    else:  # используем маскировку карты
        number_card = list(str_number_card_or_account[-16:])
        number_card_mask = get_mask_card_number(number_card)
        word = str_number_card_or_account[:-17]
        if number_card_mask == "Некорректный номер карты":
            text = "Некорректный номер карты"
        else:
            text = str(f"{word.title()} {number_card_mask}")

    return text


def get_date(str_date: str) -> str:
    """Принимает строку с датой и возвращает дату в формате "ДД.ММ.ГГГГ" """

    if str_date == "":
        return None
    else:
        # Извлекаем год, месяц и день из строки
        year = str_date[1:5]  # Год
        month = str_date[6:8]  # Месяц
        day = str_date[9:11]  # День
        return f"{day}.{month}.{year}"

