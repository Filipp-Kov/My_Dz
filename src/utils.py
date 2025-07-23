import json
import os
import logging

logger = logging.getLogger(__name__)
# Создаем хэндлер для вывода в файл
file_handler = logging.FileHandler("utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(json_file_path: str = "date/operations.json") -> list[dict]:
    """Загружает данные о транзакциях из JSON-файла"""

    logger.info("Приняли данные о транзациях из JSON-файла")

    # Проверяем, существует ли файл и не пуст ли он
    if not os.path.exists(json_file_path) or os.path.getsize(json_file_path) == 0:
        logger.error("Файл не существует или пуст")
        return []

    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что данные — это список словарей
            if isinstance(data, list):
                logger.info('Данные соответсвуют требованиям "Список словарей"')
                return data
            else:
                logger.error("Данные не являются списком словарей")
                return []

    except (json.JSONDecodeError, UnicodeDecodeError):  # Если файл битый или не JSON
        logger.error("Файл не просматривается")
        return []
