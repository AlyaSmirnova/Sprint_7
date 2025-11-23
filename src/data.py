class ResponseCodes:
    OK = 200
    CREATED = 201
    CONFLICT = 409
    BAD_REQUEST = 400
    NOT_FOUND = 404

class ResponseMessages:
    CREATE_SUCCESS = {"ok": True}
    CONFLICT_MESSAGE = "Этот логин уже используется. Попробуйте другой."
    BAD_REQUEST_MESSAGE = "Недостаточно данных для создания учетной записи"
    LOGIN_BAD_REQUEST_MESSAGE = "Недостаточно данных для входа"
    LOGIN_NOT_FOUND = "Учетная запись не найдена"
    ORDER_CREATED = {"track": ""}

VALID_COURIER = {
    'login': 'HattoriHanzo',
    'password': '123456',
    'firstName': 'Alex'
}

INVALID_COURIERS = {
    'login': 'Scorpion',
    'password': '776655'
}

ORDER_DATA = {
        'firstName': 'Alex',
        'lastName': 'Smith',
        'address': '5th Avenue, New York',
        'metroStation': 3,
        'phone': '+7 911 365 78 93',
        'rentTime': 5,
        'deliveryTime': '2025-05-05',
        'comment': 'call before'
    }

COLOR_PARAMS = [
    ({'color': ['BLACK']}, 'Black color'),
    ({'color': ['GREY']}, 'Grey color'),
    ({'color': ['BLACK', 'GREY']}, 'Both colors'),
    ({}, 'No color')
]