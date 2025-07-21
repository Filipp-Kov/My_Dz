import requests


def convert_transaction_amount(transaction: dict) -> float:
    """ Конвертирует сумму транзакции в рубли используя API конвертации валют. """
    try:
        # Проверка обязательных полей
        if "amount" not in transaction or "currency" not in transaction:
            raise ValueError("Транзакция должна содержать amount и currency")

        # Преобразование суммы
        try:
            amount = float(transaction["amount"])
        except (ValueError, TypeError):
            raise ValueError("Некорректная сумма транзакции")

        currency = transaction["currency"].upper()

        # Если валюта уже рубли
        if currency == "RUB":
            return amount

        # Проверка поддерживаемых валют
        if currency not in ("USD", "EUR"):
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

        # Запрос к API конвертации
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert",
            params={
                "to": "RUB",
                "from": currency,
                "amount": amount
            },
            headers={"apikey": "API_KEY"},
            timeout=10
        )

        # Проверка ответа
        response.raise_for_status()
        result = response.json()

        if not result.get("success", False):
            raise ValueError(f"Ошибка API: {result.get('error', {}).get('info', 'Unknown error')}")

        return round(result["result"], 2)

    except requests.RequestException as e:
        raise ValueError(f"Ошибка запроса к API: {str(e)}") from e
    except (KeyError, ValueError) as e:
        raise ValueError(f"Ошибка конвертации: {str(e)}") from e
