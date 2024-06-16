import requests
from urls import Urls
import allure
from faker import Faker


class UserApi:

    @staticmethod
    @allure.title("Генерируем пользовательские данные, возвращаем словарь с его именем, почтой, паролем")
    def generate_user_data():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        user_data = {
            "email": email,
            "password": password,
            "name": name
        }
        return user_data


    @staticmethod
    @allure.step("Зарегистрировать пользователя")
    def register_user(user_data):
        user_response = requests.post(Urls.BASE_URL_FOR_API + Urls.USER_REGISTRATION_FOR_API, json=user_data)
        return user_response

    @staticmethod
    @allure.step("Получить access token созданного пользователя")
    def get_access_token(user_response):
        access_token = user_response.json().get("accessToken")
        return access_token


    @staticmethod
    @allure.title("Удаляем пользователя по токену")
    def delete_user(access_token):
        headers = {
            "Authorization": access_token
        }
        response_delete = requests.delete(Urls.BASE_URL_FOR_API + Urls.DELETE_USER_FOR_API, headers=headers)
        return response_delete

