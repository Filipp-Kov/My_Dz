def get_mask_card_number(number_card: list) -> str:
    """Функцию маскировки номера банковской карты"""

    # Проверяем, что в списке есть хотя бы один элемент
    if not number_card or len(number_card[0]) < 16:
        return "Некорректный номер карты"

    # Получаем строку номера карты из первого элемента списка
    number_card = number_card[0]

    # Удаляем все нецифровые символы
    number_card = ''.join(filter(str.isdigit, number_card))

    if len(number_card) != 16:
        return "Некорректный номер карты"

    # Маскировка номера карты
    number_card_mask = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    return number_card_mask


def get_mask_account(number_account: list) -> str:
    """Функцию маскировки номера банковского счета"""

    # Проверяем, что в списке есть хотя бы один элемент
    if not number_account or len(number_account[0]) < 16:
        return "Некорректный номер счета"

    # Получаем строку номера карты из первого элемента списка
    number_account = number_account[0]

    # Удаляем все нецифровые символы
    number_account = ''.join(filter(str.isdigit, number_account))

    if len(number_account) != 20:
        return "Некорректный номер счета"

    # Маскировка номера счета
    number_account_mask = str(f"**{number_account[-4:]}")
    return number_account_mask
