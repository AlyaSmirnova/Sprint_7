import pytest
import requests
import allure
from src.config import Config
from src.data import ResponseCodes, ResponseMessages


class TestCourierLogin:
    @allure.title('Успешная авторизация курьера')
    def test_successful_courier_authorization(self, new_courier):
        courier_data = {
            'login': new_courier[0],
            'password': new_courier[1]
        }
        response = requests.post(f'{Config.URL}/courier/login', data = courier_data)
        assert response.status_code == ResponseCodes.OK, "Ожмдался код 200, авторизация провалена"
        assert 'id' in response.json()

    @allure.title('Проверка неуспешной авторизации при пропуске заполнения обязательного поля')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_authorization_without_necessary_field(self, new_courier, missing_field):
        courier_data = {
            'login': new_courier[0],
            'password': new_courier[1]
        }
        del courier_data[missing_field]

        response = requests.post(f'{Config.URL}/courier/login', data = courier_data)
        assert response.status_code == ResponseCodes.BAD_REQUEST, "Ожидался код 400, не все обязательные поля заполнены"
        assert response.json()['message'] == ResponseMessages.BAD_REQUEST_MESSAGE

    @allure.title('Проверка авторизации с неверным паролем')
    def test_authorization_with_incorrect_password(self, new_courier):
        courier_data = {
            'login': new_courier[0],
            'password': 'incorrect_password'
        }

        response = requests.post(f'{Config.URL}/courier/login', data = courier_data)
        assert response.status_code == ResponseCodes.BAD_REQUEST, "Ожидался код 400, неверный пароль"
        assert response.json()['message'] == ResponseMessages.BAD_REQUEST_MESSAGE


    @allure.title("Проверка авторизации несуществующего пользователя")
    def test_authorization_nonexisting_courier(self):
        courier_data = {
            'login': 'nonexisting_login',
            'password': 'nonexisting_password'
        }
        response = requests.post(f'{Config.URL}/courier/login', data = courier_data)
        assert response.status_code == ResponseCodes.NOT_FOUND, "Ожидался код 404, несуществующий пользователь"
        assert response.json()['message'] == ResponseMessages.LOGIN_NOT_FOUND
