import json
import os


def load_transactions(json_file_path: str = "date/operations.json") -> list[dict]:
    """Загружает данные о транзакциях из JSON-файла"""

    # Проверяем, существует ли файл и не пуст ли он
    if not os.path.exists(json_file_path) or os.path.getsize(json_file_path) == 0:
        return []

    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что данные — это список словарей
            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, UnicodeDecodeError):  # Если файл битый или не JSON
        return []
