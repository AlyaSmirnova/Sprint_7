import requests
import allure
from src.config import Config
from src.data import ResponseCodes

class TestOrderList:
    @allure.title('Проверка получения списка заказов')
    def test_get_orders_list(self):
        response = requests.get(f'{Config.URL}{Config.ORDER_URL}')
        assert response.status_code == ResponseCodes.OK, "Ожидался код 200, список заказов не получен"
        assert isinstance(response.json()['orders'], list)
        assert len(response.json()['orders']) > 0
