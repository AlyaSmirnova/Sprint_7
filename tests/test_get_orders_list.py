import requests
import allure
from src.config import Config
from src.data import ResponseCodes

class TestOrderList:
    @allure.title('Проверка получения списка заказов')
    def test_get_orders_list(self, new_order):
        response = requests.get(Config.URL)
        assert response.status_code == ResponseCodes.OK, "Ожидался код 200, список заказов не получен"
        assert isinstance(response.json()['orders'], list)
        assert len(response.json()['orders']) > 0