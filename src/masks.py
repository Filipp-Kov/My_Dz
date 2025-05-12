def get_mask_card_number(number_card: list) -> str:
    """Функцию маскировки номера банковской карты"""

    number_card_mask = str(f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}")
    return number_card_mask


def get_mask_account(number_account: list) -> str:
    """Функцию маскировки номера банковского счета"""

    number_account_mask = str(f"**{number_account[-4:]}")
    return number_account_mask
