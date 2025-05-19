from widget import get_date


def filter_by_state(list_dictionaries: list, state="EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список словарей в которых содержится значение state"""

    list_dictionaries_state = []

    for i in list_dictionaries:
        if i["state"] == state:
            list_dictionaries_state.append(i)

    return list_dictionaries_state


def sort_by_date(list_dictionaries: list, fun_sorted: bool = False) -> list:
    """Функция принимает список словарей и сортирует их по дате. Параметр сортировки по умолчанию - убывание"""

    sorted_list = sorted(list_dictionaries, key=lambda x: get_date(x["date"]), reverse=not fun_sorted)

    return sorted_list
