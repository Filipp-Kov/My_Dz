def filter_by_currency(transactions, currency):
    """ Фильтрует транзакции по заданной валюте и возвращает итератор. """

    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions):
    """ Принимает список словарей с транзакциями и возвращает описание каждой операции """

    for transaction in transactions:
        transaction_info = transaction.get("description", {})
        yield transaction_info


def card_number_generator(start_range, end_range):
    if start_range < 1 or end_range > 9999999999999999:
        return "Некорректный диапазон. Допустимые значения: от 1 до 9999999999999999."

    for number in range(start_range, end_range + 1):
        # Преобразуем число в строку, дополняем нулями до 16 символов
        card_str = str(number).zfill(16)

        # Разбиваем на 4 блока по 4 цифры и соединяем пробелами
        formatted_card = ' '.join([
            card_str[0:4],
            card_str[4:8],
            card_str[8:12],
            card_str[12:16]
        ])

        yield formatted_card

