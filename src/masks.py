import logging

logger = logging.getLogger(__name__)
# Создаем хэндлер для вывода в файл
file_handler = logging.FileHandler("masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: list) -> str:
    """Функцию маскировки номера банковской карты"""

    logger.info("Приняли номер карты")

    # Проверяем, что в списке есть хотя бы один элемент
    # if not number_card or len(number_card[0]) < 16:
    #     return "Некорректный номер карты"

    # # Получаем строку номера карты из первого элемента списка
    # number_card = number_card[0]

    # Удаляем все нецифровые символы
    number_card = "".join(filter(str.isdigit, number_card))
    logger.info("Удалили все нецифровые символы")

    if len(number_card) != 16:
        logger.error("Получили не корректный номер карты")
        return "Некорректный номер карты"

    # Маскировка номера карты
    number_card_mask = f"{number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
    logger.info(f"Вывели замаскированный номер карты {number_card_mask}")
    return number_card_mask


def get_mask_account(number_account: list) -> str:
    """Функцию маскировки номера банковского счета"""

    logger.info("Получили номер счета")

    # Проверяем, что в списке есть хотя бы один элемент
    # if not number_account or len(number_account[0]) < 20:
    #     return "Некорректный номер счета"

    # # Получаем строку номера карты из первого элемента списка
    # number_account = number_account[0]

    # Удаляем все нецифровые символы
    number_account = "".join(filter(str.isdigit, number_account))
    logger.info("Удалили все нецифровые символы")

    if len(number_account) != 20:
        logger.error("Получили некорректный номер счета")
        return "Некорректный номер счета"

    # Маскировка номера счета
    number_account_mask = str(f"**{number_account[-4:]}")
    ogger.info(f"Вывели замаскированный номер счета {number_account_mask}")
    return number_account_mask
