from urls import Urls
from locators import BasePageLocators, LoginPage, AccountPage
from conftest import driver
import allure
from pages.login_page import LoginPageStellarBurgers
class TestLoginPage:

    @allure.title('Авторизация на странице логина')
    @allure.description(
        'Проверка возможности авторизоваться пользователем')
    def test_login_into_account_page(self, driver):
        driver, user_data, user_session = driver
        login_page = LoginPageStellarBurgers(driver, user_data)
        login_page.wait_and_find_element(BasePageLocators.account_profile_link)
        login_page.element_click_new(BasePageLocators.account_profile_link)
        assert login_page.get_url() == Urls.LOGIN_PAGE
        login_page.login_with_fixture_data()
        assert login_page.wait_and_find_element(BasePageLocators.make_order_button).is_displayed()

    @allure.title('Отображение раздела История заказов в личном кабинете')
    @allure.description(
        'Проверка отображения раздела История заказов в личном кабинете авторизованного пользователя')
    def test_check_history_in_account_page(self, driver):
        driver, user_data, user_session = driver
        login_page = LoginPageStellarBurgers(driver, user_data)
        login_page.wait_and_find_element(BasePageLocators.login_button)
        login_page.element_click_new(BasePageLocators.login_button)
        assert login_page.get_url() == Urls.LOGIN_PAGE
        login_page.login_with_fixture_data()
        login_page.wait_and_find_element(BasePageLocators.account_profile_link)
        login_page.element_click(BasePageLocators.account_profile_link)
        login_page.wait_and_find_element(AccountPage.orders_history_link)
        login_page.element_click_new(AccountPage.orders_history_link)
        assert login_page.get_url() == Urls.ACCOUNT_ORDERS_HISTORY_PAGE

    @allure.title('Авторизованный пользователь может разлогиниться')
    @allure.description(
        'Проверка возможности выхода авторизованного пользователя из учетной записи и перенаправление его на авторизационную страницу')
    def test_authorized_user_can_logout(self, driver):
        driver, user_data, user_session = driver
        login_page = LoginPageStellarBurgers(driver, user_data)
        login_page.wait_and_find_element(BasePageLocators.login_button)
        login_page.element_click_new(BasePageLocators.login_button)
        assert login_page.get_url() == Urls.LOGIN_PAGE
        login_page.login_with_fixture_data()
        login_page.wait_and_find_element(BasePageLocators.account_profile_link)
        login_page.element_click(BasePageLocators.account_profile_link)
        login_page.wait_and_find_element(AccountPage.logout_button)
        login_page.element_click(AccountPage.logout_button)
        login_page.wait_and_find_element(LoginPage.login_button)
        assert login_page.get_url() == Urls.LOGIN_PAGE

    @allure.title('Авторизованный пользователь может сделать заказ')
    @allure.description(
        'Проверка возможности авторизованного пользователя оформить заказ, отображение кнопки Оформить заказ')
    def test_authorized_user_can_do_order(self, driver):
        driver, user_data, user_session = driver
        login_page = LoginPageStellarBurgers(driver, user_data)
        login_page.wait_and_find_element(BasePageLocators.login_button)
        login_page.element_click_new(BasePageLocators.login_button)
        assert login_page.get_url() == Urls.LOGIN_PAGE
        login_page.login_with_fixture_data()
        assert login_page.wait_and_find_element(BasePageLocators.make_order_button).is_displayed()





