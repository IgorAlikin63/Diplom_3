from conftest import driver
import allure
from locators import LoginPage
from pages.base_page import BasePageStellarBurgers
class LoginPageStellarBurgers(BasePageStellarBurgers):

    @allure.step("Вызываем базовый конструктор LoginPageStellarBurgers")
    def __init__(self, driver, user_data):
        super().__init__(driver)
        self.user_data = user_data

    @allure.step("Ввести данные пользователя и выполнить вход используя данные, которые генерирует фикстура создания пользователя")
    def login_with_fixture_data(self):
        #Ввод почты
        self.send_keys_in_input(LoginPage.email_field, self.user_data['email'])
        #Ввод пароля
        self.send_keys_in_input(LoginPage.password_field, self.user_data['password'])
        #Нажатие кнопки входа
        self.element_click_new(LoginPage.login_button)


