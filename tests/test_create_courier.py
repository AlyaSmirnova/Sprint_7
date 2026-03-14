import pytest
import requests
import allure
from src.config import Config
from src.data import ResponseCodes, ResponseMessages


@allure.feature('Courier Management')
@allure.story('Courier Creation')
class TestCourierCreation:

    @allure.title('Create courier successfully')
    @allure.description('Verify that a courier can be created with all valid required fields')
    def test_successful_courier_creation(self, new_courier):
        response = requests.post(f'{Config.URL}{Config.COURIER_URL}', data = new_courier)
        assert response.status_code == ResponseCodes.CREATED, f"Expected 201, but got {response.status_code}"
        assert response.json() == ResponseMessages.CREATE_SUCCESS, f"Expected success message, but got {response.json()}"

    @allure.title('Create duplicate courier')
    @allure.description('Verify that it is impossible to create two couriers with the same login')
    def test_unsuccessful_duplicate_courier_creation(self, new_courier):
        requests.post(f'{Config.URL}{Config.COURIER_URL}', data=new_courier)
        duplicate_response = requests.post(f'{Config.URL}{Config.COURIER_URL}', data = new_courier)
        assert duplicate_response.status_code == ResponseCodes.CONFLICT, f"Expected 409 for duplicate, but got {duplicate_response.status_code}"
        assert duplicate_response.json()['message'] == ResponseMessages.CONFLICT_MESSAGE

    @allure.title('Check required fields for courier creation')
    @allure.description('Verify that courier cannot be created if login or password is missing')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_cannot_create_courier_without_all_necessary_fields(self, new_courier, field):
        test_data = new_courier.copy()
        del test_data[field]
        response = requests.post(f'{Config.URL}{Config.COURIER_URL}', data = test_data)
        assert response.status_code == ResponseCodes.BAD_REQUEST, f"Expected 400 for missing {field}, but got {response.status_code}"
        assert response.json() ['message'] == ResponseMessages.BAD_REQUEST_MESSAGE
