import pytest
import requests
import allure

class TestOrderList:
    URL = "https://qa-scooter.praktikum-services.ru/api/v1"
    @allure.title('Проверка получения списка заказов')
    def test_get_orders_list(self, new_order):
        response = requests.get(self.URL)
        assert response.status_code == 200, "Ожидался код 200, список заказов не получен"
        assert isinstance(response.json()['orders'], list)
        assert len(response.json()['orders']) > 0