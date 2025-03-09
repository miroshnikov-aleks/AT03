import requests

def get_cat_image():
    """
    Делает запрос к TheCatAPI для получения случайного изображения кошки.
    Возвращает URL изображения или None при ошибке.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]['url']  # URL изображения находится в первом элементе списка
        else:
            return None
    except requests.exceptions.RequestException:
        return None