import unittest
from unittest.mock import mock_open, patch
from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}, {"id": 2}]')
    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=10)
    def test_load_valid_json(self, mock_size, mock_exists, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [{"id": 1}, {"id": 2}])

    @patch("os.path.exists", return_value=False)
    def test_file_not_found(self, mock_exists):
        result = load_transactions("invalid_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=0)
    def test_empty_file(self, mock_size, mock_exists, mock_file):
        result = load_transactions("empty.json")
        self.assertEqual(result, [])
