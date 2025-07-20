import requests


def convert_transaction_amount(transaction: dict) -> float:
    """Конвертация суммы транзакции в рубли с использованием API"""
    try:
        if "amount" not in transaction or "currency" not in transaction:
            raise ValueError("Transaction must contain amount and currency")

        amount = float(transaction["amount"])
        currency = transaction["currency"].upper()

        if currency == "RUB":
            return amount

        if currency not in ("USD", "EUR"):
            raise ValueError(f"Unsupported currency: {currency}")

        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/latest",
            params={"base": currency, "symbols": "RUB"},
            headers={"apikey": "API_KEY"},
            timeout=5,
        )
        response.raise_for_status()
        rate = response.json()["rates"]["RUB"]
        return round(amount * rate, 2)

    except (ValueError, requests.RequestException, KeyError) as e:
        raise ValueError(f"Currency conversion failed: {str(e)}") from e
