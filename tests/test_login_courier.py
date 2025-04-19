import pytest
import allure

from conftest import auth_courier


@allure.title('Успешная авторизация курьера')
def test_successful_courier_authorization(new_courier):
    courier_data = {
        'login': new_courier[0],
        'password': new_courier[1]
    }
    response = auth_courier(courier_data)
    assert response.status_code == 200, "Ожмдался код 200, авторизация провалена"
    assert 'id' in response.json()

@allure.title('Проверка неуспешной авторизации при пропуске заполнения обязательного поля')
@pytest.mark.parametrize('missing_field', ['login', 'password'])
def test_authorization_without_necessary_field(new_courier, missing_field):
    courier_data = {
        'login': new_courier[0],
        'password': new_courier[1]
    }
    del courier_data[missing_field]

    response = auth_courier(courier_data)
    assert response.status_code == 400, "Ожидался код 400, не все обязательные поля заполнены"
    assert "Недостаточно данных для входа" in response.text

@allure.title('Проверка авторизации с неверным паролем')
def test_authorization_with_incorrect_password(new_courier):
    courier_data = {
        'login': new_courier[0],
        'password': 'incorrect_password'
    }

    response = auth_courier(courier_data)
    assert response.status_code == 404, "Ожидался код 404, неверный пароль"
    assert "Учетная запись не найдена" in response.text


@allure.title("Проверка авторизации несуществующего пользователя")
def test_authorization_nonexisting_courier():
    courier_data = {
        'login': 'nonexisting_login',
        'password': 'nonexisting_password'
    }
    response = auth_courier(courier_data)
    assert response.status_code == 404, "Ожидался код 404, несуществующий пользователь"
    assert "Учетная запись не найдена" in response.text
