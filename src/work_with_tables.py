import pandas as pd


file_path_csv = "transactions.csv"
file_path_excel = "date/transactions_excel.xlsx"

def work_with_csv(file_path_csv):
    ''' Функция принимает оперции из CSV файла и выдает список словарей с транзакциями '''

    try:
        # Читаем CSV файл с помощью pandas
        transactions_df = pd.read_csv(file_path_csv)

        # Конвертируем DataFrame в список словарей
        transactions_list = transactions_df.to_dict('records')

        return transactions_list

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path_csv} не найден")
        return []
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {file_path_csv} пустой")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")
        return []


def work_with_excel(file_path_excel):
    """Функция принимает Excel файл с финансовыми операциями и возвращает список словарей"""
    try:
        # Читаем Excel файл с помощью pandas
        transactions_df = pd.read_excel(file_path_excel) 

        # Конвертируем DataFrame в список словарей
        transactions_list = transactions_df.to_dict("records")

        return transactions_list

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path_excel} не найден")
        return []
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {file_path_excel} пустой")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")
        return []
