import requests
import allure

URL = "https://qa-scooter.praktikum-services.ru/api/v1"

@allure.title('Успешное создание курьера')
def test_successfull_courier_creation(new_courier):
    assert len(new_courier) == 3, "Неверное количество данных в ответе"
    # проверяем, что вернулось 3 элемента, т.е. курьер был создан
    login, password, first_name = new_courier
    assert all([login, password, first_name]), "Все поля должны быть заполнены данными"
    payload = {
        'login': new_courier[0],
        'password': new_courier[1],
        'firstName': new_courier[2]
    }
    response = requests.post(f'{URL}/courier', data = payload)
    assert response.status_code == 201, "Ожидался код 201, учетная запись не создана"
    assert response.json() == {'ok': True}, "Ожидался ответ {'ok': true}"

@allure.title('Попытка создания дубликата курьера')
def test_unsuccessful_duplicate_courier_creation(new_courier):
    existing_login = new_courier[0]
    duplicate_response = requests.post(f'{URL}/courier', data = {
        'login': existing_login,
        'password': 'new_password',
        'firstName': 'new_first_name'
    })
    assert duplicate_response.status_code == 409, "Ожидался код 409, повторное создание существующего пользователя"
    assert "Этот логин уже используется" in duplicate_response.text

@allure.title('Проверяем заполнение обязательных полей при создании курьера')
def test_cannot_create_courier_without_all_necessary_fields(new_courier):
    correct_login, correct_password, correct_first_name = new_courier
    test_cases = [
        {'missing_field': 'login',
         'payload': {'password': correct_password,
                     'firstName': correct_first_name}},
        {'missing_field': 'password',
         'payload': {'login': correct_login,
                     'firstName': correct_first_name
         }},
        {'missing_field': 'firstName',
         'payload': {'login': correct_login,
                     'password': correct_password}}
    ]

    for case in test_cases:
        response = requests.post(f'{URL}/courier', data = case['payload'])
        assert response.status_code == 400, "Ожидался код 400, не все поля заполнены"
        assert 'Недостаточно данных для создания учетной записи' in response.text



#auth_response = requests.post(f'{URL}/courier/login', data={'login': login, 'password': password})
    #assert auth_response.status_code == 200, "Должна быть успешная авторизация"
    #assert 'id' in auth_response.json(), "В ответе должен отображаться id курьера"
    # проверяем, что при попытке авторизоваться с получеными логином и паролем авторизация проходит
