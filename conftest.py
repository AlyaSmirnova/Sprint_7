import pytest
import requests
import allure
from src.config import Config
from src.helpers import register_new_courier_and_return_login_password
from src.data import ResponseCodes, VALID_COURIER, INVALID_COURIERS, ORDER_DATA


# фикстура создает нового курьера
@pytest.fixture
def new_courier():
    with allure.step('Создание нового курьера'):
        courier_data = register_new_courier_and_return_login_password()
        login = courier_data[0] + '_test'
        password = courier_data[1]
        first_name = courier_data[2] if len(courier_data) > 2 else ""

        courier_payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        yield courier_payload

        with allure.step("Удаление тестового курьера"):
            login, password = courier_data[0], courier_data[1]
            payload = {
                'login': login,
                'password': password
            }
            login_response = requests.post(f'{Config.URL}{Config.COURIER_LOGIN_URL}', data = payload)
            if login_response.status_code == ResponseCodes.OK:
                courier_id = login_response.json().get('id')
                requests.delete(f'{Config.URL}/courier/{courier_id}')

# фикстура дает корректные данные для создания курьера
@pytest.fixture
def auth_courier():
    return VALID_COURIER.copy()

# фикстура дает неверные учетные данные
@pytest.fixture
def unauth_courier():
    return INVALID_COURIERS.copy()

@pytest.fixture
def new_order():
    response = requests.post(f'{Config.URL}{Config.ORDER_URL}', json=ORDER_DATA)
    track = response.json()['track']
    yield {'track': track, 'order_data': ORDER_DATA}