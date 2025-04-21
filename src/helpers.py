import requests
import allure
import random
import string
from src.config import Config


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    @allure.step('Генерация случайной строки длиной {length}')
    def generate_random_string(length):
        letters = string.ascii_lowercase # это константа из модуля string, которая содержит все буквы английского алфавита в нижнем регистре
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
        # возвращаем полученную случайную строку

    # создаём список, чтобы метод мог его вернуть
    login_pass = []
    with allure.step('Готовим данные для создания курьера'):
        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        # создает случайный логин из 10 букв
        password = generate_random_string(10)
        # создает случайный пароль из 10 букв
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    # ключи словаря соответствуют ожидаемой API-структуре
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{Config.URL}/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass