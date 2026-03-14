import pytest
import requests
import allure
from src.config import Config
from src.data import ResponseCodes, ResponseMessages, ORDER_DATA, COLOR_PARAMS


@allure.feature('Order Management')
@allure.story('Order Creation')
class TestOrderCreation:
    @allure.title('Create order with color variation: {title}')
    @allure.description('Verify that an order can be successfully created with different color selections (or no color)')
    @pytest.mark.parametrize('color_params, title', COLOR_PARAMS)
    def test_create_order_with_color_params(self, color_params, title):
        order_data = {**ORDER_DATA, **color_params}
        with allure.step(f'Send POST request to create order with {title}'):
            response = requests.post(f'{Config.URL}{Config.ORDER_URL}', json=order_data)
        with allure.step('Verify response status code and track number'):
            assert response.status_code == ResponseCodes.CREATED, f"Expected 201, but got {response.status_code}. Response: {response.text}"
            response_data = response.json()
            assert 'track' in response_data, "Response does not contain 'track' number"
            assert isinstance(response_data['track'], int), "Track number must be an integer"
