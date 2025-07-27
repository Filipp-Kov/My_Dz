import requests
import unittest
from unittest.mock import patch
from src.external_api import convert_transaction_amount


class TestConvertTransactionAmount(unittest.TestCase):

    def test_rub_transaction(self):
        transaction = {"amount": "100.00", "currency": "RUB"}
        result = convert_transaction_amount(transaction)
        self.assertEqual(result, 100.00)

    @patch("requests.get")
    def test_usd_conversion(self, mock_get):
        # Настраиваем мок для API
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {"rates": {"RUB": 75.50}}
        mock_get.return_value = mock_response

        transaction = {"amount": "100.00", "currency": "USD"}
        result = convert_transaction_amount(transaction)
        self.assertEqual(result, 7550.00)  # 100 * 75.50

    @patch("requests.get")
    def test_api_failure(self, mock_get):
        # Настраиваем мок для вызова исключения при запросе
        mock_get.side_effect = requests.RequestException("API error")

        transaction = {"amount": "100.00", "currency": "USD"}

        with self.assertRaises(ValueError) as context:
            convert_transaction_amount(transaction)

        self.assertIn("Currency conversion failed: API error", str(context.exception))

    def test_invalid_transaction(self):
        with self.assertRaises(ValueError):
            convert_transaction_amount({"amount": "100.00"})  # Нет currency
