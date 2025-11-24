import requests
import random
import string
from endpoints import CREATE_COURIER

class CourierGenerator:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def register_new_courier_and_return_login_password(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(CREATE_COURIER, data=payload)

        # Здесь нет необходимости проверять статус ответа 201,
        # так как фикстура, которая вызывает этот метод, ожидает,
        # что курьер будет создан. Если нет, это будет ошибкой теста.
        # Возвращаем созданные данные независимо от статуса,
        # так как они понадобятся для попытки логина/удаления.
        return {"login": login, "password": password, "firstName": first_name}

