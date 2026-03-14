import requests
import allure
from src.config import Config
from src.data import ResponseCodes

@allure.feature('Order Management')
@allure.story('Get Order List')
class TestOrderList:
    @allure.title('Retrieve all existing orders')
    @allure.description('Verify that the list of orders can be successfully retrieved and is not empty')
    def test_get_orders_list(self):
        with allure.step(f'Send GET request to {Config.ORDER_URL}'):
            response = requests.get(f'{Config.URL}{Config.ORDER_URL}')
        with allure.step('Verify response status and order list structure'):
            assert response.status_code == ResponseCodes.OK, f"Expected 200 OK, but got {response.status_code}. Response: {response.text}"
        response_data = response.json()
        assert 'orders' in response_data, "Response does not contain 'orders' key"
        assert isinstance(response_data['orders'], list), "'orders' should be a list"
        assert len(response_data['orders']) > 0, "The order list is empty, expected at least one record"
