from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
import allure
from user_api import UserApi
from urls import Urls


class TestLoginPage:

    @allure.title('Авторизация на странице логина')
    @allure.description(
        'Проверка возможности авторизоваться пользователем')
    def test_login_into_account_page(self, driver):
        user_data = UserApi.generate_user_data()
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title()
        main_page.click_account_button()
        assert personal_account_page.check_account_description_changes()
        access_token = UserApi.get_access_token(user_response)
        UserApi.delete_user(access_token)

    @allure.title('Отображение раздела История заказов в личном кабинете')
    @allure.description(
        'Проверка отображения раздела История заказов в личном кабинете авторизованного пользователя')
    def test_check_history_in_account_page(self, driver):
        user_data = UserApi.generate_user_data()
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title()
        main_page.click_account_button()
        personal_account_page.click_order_history_button()
        current_url = personal_account_page.check_current_url_after_action_in_personal_account_page()
        assert current_url == Urls.ACCOUNT_ORDERS_HISTORY_PAGE
        access_token = UserApi.get_access_token(user_response)
        UserApi.delete_user(access_token)

    @allure.title('Авторизованный пользователь может разлогиниться')
    @allure.description(
        'Проверка возможности выхода авторизованного пользователя из учетной записи и перенаправление его на авторизационную страницу')
    def test_authorized_user_can_logout(self, driver):
        user_data = UserApi.generate_user_data()
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title()
        main_page.click_account_button()
        personal_account_page.click_logout_button()
        personal_account_page.find_login_page_title()
        current_url = personal_account_page.check_current_url_after_action_in_personal_account_page()
        assert current_url == Urls.LOGIN_PAGE
        access_token = UserApi.get_access_token(user_response)
        UserApi.delete_user(access_token)








