from typing import List, Dict, Any
from src.widget import get_date


def filter_by_state(list_of_transactions: List[Dict[str, Any]], state="EXECUTED") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список словарей в которых содержится значение state"""

    list_of_transactions_state = []

    for i in list_of_transactions:
        if i["state"] == state:
            list_of_transactions_state.append(i)

    return list_of_transactions_state


def sort_by_date(list_of_transactions: List[Dict[str, Any]], fun_sorted: bool = False) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и сортирует их по дате. Параметр сортировки по умолчанию - убывание"""
    # Фильтруем некорректные даты
    filtered_transactions = [tx for tx in list_of_transactions if get_date(tx["date"]) is not None]

    sorted_list = sorted(filtered_transactions, key=lambda x: get_date(x["date"]), reverse=not fun_sorted)

    return sorted_list
