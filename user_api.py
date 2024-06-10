import requests
from urls import Urls
import allure
from faker import Faker


class UserSession:
    def __init__(self):
        self.accessToken = None

# Создаем экземпляр класса UserSession для хранения accessToken
user_session = UserSession()

class UserApi:

    @staticmethod
    @allure.step('Регистрируем нового юзера со случайными данными, возвращаем словарь с его именем, почтой, паролем')
    def register_new_user_and_return_email_password():
        # генерируем почту, пароль и имя курьера
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Urls.BASE_URL_FOR_API + Urls.USER_REGISTRATION_FOR_API, json=payload)

        # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль курьера
        if response.status_code == 200:
            user_data = {
                "email": email,
                "password": password,
                "name": name
            }
            return user_data  # Возвращаем словарь данных пользователя

            # если возникла ошибка, возвращаем пустой словарь
        else:
            return {}


    @staticmethod
    @allure.step('Авторизуем юзера и получаем его accessToken')
    def login_user(user_session, email, password):
        login_payload = {
            "email": email,
            "password": password
       }
        response_login = requests.post(Urls.BASE_URL_FOR_API + Urls.USER_LOGIN_FOR_API, json=login_payload)
        if response_login.status_code == 200:
            user_session.accessToken = response_login.json()['accessToken']
            return user_session
        else:
            print(f"Ошибка: {response_login.status_code}")
            print(response_login.json())
            return None


    @staticmethod
    @allure.step('Удаляем пользователя по токену')
    def delete_user(user_session):
        headers = {
            "Authorization": user_session.accessToken
        }
        response = requests.delete(Urls.BASE_URL_FOR_API + Urls.DELETE_USER_FOR_API, headers=headers)
        if response.status_code == 202:
            return {"success": True , "message": "User successfully removed"}
        else:
            print(f"Ошибка при удалении пользователя: {response.status_code}")
            print(f"Тело ответа: {response.json()}")
            return {'success': False, 'message': 'Failed to delete user', 'error': response.json()}

