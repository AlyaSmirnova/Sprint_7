import pytest
import requests
import allure
from src.config import Config
from src.data import ResponseCodes, ResponseMessages


@allure.feature('Courier Management')
@allure.story('Courier Authorization')
class TestCourierLogin:
    @allure.title('Successful courier authorization')
    @allure.description('Verify that a courier can log in with valid credentials and receive an ID')
    def test_successful_courier_authorization(self, new_courier):
        with allure.step('Register a new courier'):
            requests.post(f'{Config.URL}{Config.COURIER_URL}', data=new_courier)
        courier_data = {
            'login': new_courier['login'],
            'password': new_courier['password']
        }
        with allure.step('Send login request'):
            response = requests.post(f'{Config.URL}{Config.COURIER_LOGIN_URL}', data = courier_data)
        with allure.step('Verify response status and presence of ID'):
            assert response.status_code == ResponseCodes.OK, f"Expected 200 OK, but got {response.status_code}"
            assert 'id' in response.json(), "Response does not contain courier ID"

    @allure.title('Authorization fails if required field is missing: {missing_field}')
    @allure.description('Verify that login fails with 400 error if login or password field is empty')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_authorization_without_necessary_field(self, new_courier, missing_field):
        courier_data = {
            'login': new_courier['login'],
            'password': new_courier['password']
        }
        courier_data[missing_field] = ''

        with allure.step(f'Send login request with empty {missing_field}'):
            response = requests.post(f'{Config.URL}{Config.COURIER_LOGIN_URL}', data = courier_data)
        with allure.step('Verify 400 Bad Request error'):
            assert response.status_code == ResponseCodes.BAD_REQUEST, f"Expected 400 for empty {missing_field}"
            assert response.json()['message'] == ResponseMessages.LOGIN_BAD_REQUEST_MESSAGE

    @allure.title('Authorization with incorrect password')
    @allure.description('Verify that login fails with 404 error if password is incorrect')
    def test_authorization_with_incorrect_password(self, new_courier):
        courier_data = {
            'login': new_courier['login'],
            'password': 'incorrect_password'
        }

        with allure.step('Send login request with wrong password'):
            response = requests.post(f'{Config.URL}/courier/login', data = courier_data)
        with allure.step('Verify 404 Not Found error'):
            assert response.status_code == ResponseCodes.NOT_FOUND, "Expected 404 for incorrect password"
            assert response.json()['message'] == ResponseMessages.LOGIN_NOT_FOUND

    @allure.title('Authorization of non-existing courier')
    @allure.description('Verify that login fails with 404 error for non-existing credentials')
    def test_authorization_not_existing_courier(self):
        courier_data = {
            'login': 'not_existing_login',
            'password': 'not_existing_password'
        }

        with allure.step('Send login request for non-existing user'):
            response = requests.post(f'{Config.URL}/courier/login', data = courier_data)
        with allure.step('Verify 404 Not Found error'):
            assert response.status_code == ResponseCodes.NOT_FOUND, "Expected 404 for non-existing user"
            assert response.json()['message'] == ResponseMessages.LOGIN_NOT_FOUND
