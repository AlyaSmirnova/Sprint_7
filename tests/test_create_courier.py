import pytest
import requests
import allure
from src.config import Config
from src.data import ResponseCodes, ResponseMessages

class TestCourierCreation:

    @allure.title('Успешное создание курьера')
    def test_successful_courier_creation(self, new_courier):
        response = requests.post(f'{Config.URL}{Config.COURIER_URL}', data = new_courier)
        assert response.status_code == ResponseCodes.CREATED, "Ожидался код 201, учетная запись не создана"
        assert response.json() == ResponseMessages.CREATE_SUCCESS, "Ожидался ответ {'ok': true}"

    @allure.title('Попытка создания дубликата курьера')
    def test_unsuccessful_duplicate_courier_creation(self, new_courier):
        response = requests.post(f'{Config.URL}{Config.COURIER_URL}', data=new_courier)
        duplicate_response = requests.post(f'{Config.URL}{Config.COURIER_URL}', data = new_courier)
        assert duplicate_response.status_code == ResponseCodes.CONFLICT, "Ожидался код 409, повторное создание существующего пользователя"
        assert duplicate_response.json()['message'] == ResponseMessages.CONFLICT_MESSAGE

    @allure.title('Проверяем заполнение обязательных полей при создании курьера')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_cannot_create_courier_without_all_necessary_fields(self, new_courier, field):
        test_data = new_courier.copy()
        del test_data[field]
        response = requests.post(f'{Config.URL}{Config.COURIER_URL}', data = test_data)
        assert response.status_code == ResponseCodes.BAD_REQUEST, "Ожидался код 404, недостаточно данных для создания учетной записи"
        assert response.json() ['message'] == ResponseMessages.BAD_REQUEST_MESSAGE
