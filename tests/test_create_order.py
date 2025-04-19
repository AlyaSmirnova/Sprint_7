import pytest
import requests
import allure

URL = "https://qa-scooter.praktikum-services.ru/api/v1"

class TestOrderCreation:
    order_data = {
        'firstName': 'Alex',
        'lastName': 'Smith',
        'address': '5th Avenue, New York',
        'metroStation': 3,
        'phone': '+7 911 365 78 93',
        'rentTime': 5,
        'deliveryTime': '2025-05-05',
        'comment': 'call before'
    }

@pytest.mark.parametrize('color_params', [
    pytest.param(['BLACK'], id='only_black_color'),
    pytest.param(['GRAY'], id = 'only_gray_color'),
    pytest.param(['BLACK', 'GRAY'], id = 'both_color'),
    pytest.param([], id = 'empty_color'),
    pytest.param(None, id = 'color_param_missing')
])
    @allure.title('Проверка создания заказа с разными вариантами выбора цвета')
    def test_create_order_with_color_params(self, color_params):
        order_data = self.order_data.copy()
        if color_params is not None:
            order_data['color'] = color_params

        response = requests.post(f'{URL}/orders', json=order_data)
        assert response.status_code == 201, "Ожидался код 201, заказ не создан"
        response_json = response.json()
        assert 'track' in response_json, "В ответе нет 'track'"