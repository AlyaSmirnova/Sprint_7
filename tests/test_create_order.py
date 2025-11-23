import pytest
import requests
import allure
from src.config import Config
from src.data import ResponseCodes, ResponseMessages, ORDER_DATA, COLOR_PARAMS


class TestOrderCreation:
    @allure.title('Проверка создания заказа с разными вариантами выбора цвета')
    @pytest.mark.parametrize('color_params, title', COLOR_PARAMS)
    def test_create_order_with_color_params(self, color_params, title):
        order_data = {**ORDER_DATA, **color_params}
        response = requests.post(f'{Config.URL}{Config.ORDER_URL}', json=order_data)
        assert response.status_code == ResponseCodes.CREATED, "Ожидался код 201, заказ не создан"
        response_data = response.json()
        assert 'track' in response_data, "Заказ не найден в ответе API"
        assert isinstance(response_data['track'], int), "Номер заказа должен быть числом"
