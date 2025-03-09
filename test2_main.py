import pytest
from unittest.mock import patch
from main import get_cat_image


def test_get_cat_image_failure():
    """
    Тест проверяет неуспешный запрос (например, статус код 404) и возврат None.
    """
    with patch('requests.get') as mock_get:
        # Настройка мока для неуспешного ответа
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = None

        # Вызов функции
        result = get_cat_image()

        # Проверка результата
        assert result is None