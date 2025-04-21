import pytest
import requests
import allure
from src.config import Config
from src.helpers import register_new_courier_and_return_login_password
from src.data import ResponseCodes, ResponseMessages, VALID_COURIER, INVALID_COURIERS


# фикстура создает нового курьера
@pytest.fixture
def new_courier():
    with allure.step('Создание нового курьера'):
        courier_data = register_new_courier_and_return_login_password()
        yield courier_data

        with allure.step("Удаление тестового курьера"):
            login, password = courier_data[0], courier_data[1]
            payload = {
                'login': login,
                'password': password
            }
            login_response = requests.post(f'{Config.URL}/courier/login', data = payload)
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
