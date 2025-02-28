"""#2"""

import unittest
from unittest.mock import patch, Mock
import requests


class WebService:
    """Клас для взаємодії з вебсервісом."""

    @staticmethod
    def get_data(url: str) -> dict:
        """
        Повертає json дані з запиту.

        Arguments:
            url (str): URL вебсервісу для запиту даних.
        """
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


class TestWebService(unittest.TestCase):
    # Тестування отримання даних від вебсервісу, код 200.
    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response
        
        result = WebService.get_data("http://example.com")
        self.assertEqual(result, {"data": "test"})


    # Тестування отримання даних від вебсервісу, код 404.
    @patch('requests.get')
    def test_get_data_404_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response
        
        with self.assertRaises(requests.HTTPError):
            WebService.get_data("http://example.com")


    # Тестування отримання даних від вебсервісу, код 500.
    @patch('requests.get')
    def test_get_data_other_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.HTTPError("500 Internal Server Error")
        mock_get.return_value = mock_response
        
        with self.assertRaises(requests.HTTPError):
            WebService.get_data("http://example.com")


if __name__ == "__main__":
    unittest.main()
