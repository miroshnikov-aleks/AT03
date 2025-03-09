import pytest
from unittest.mock import patch
from main import get_cat_image


def test_get_cat_image_success():
    """
    Тест проверяет успешный запрос к TheCatAPI и возврат правильного URL.
    """
    # Моковые данные для успешного ответа
    mock_response_data = [
        {
            "url": "https://example.com/cat.jpg",
            "id": "123",
            "width": 500,
            "height": 500
        }
    ]

    with patch('requests.get') as mock_get:
        # Настройка мока для успешного ответа
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        # Вызов функции
        result = get_cat_image()

        # Проверка результата
        assert result == "https://example.com/cat.jpg"