from urls import Urls
from locators import PasswordRecoveryPage, LoginPage, ResetPasswordPage
from conftest import driver
import allure
from pages.base_page import BasePageStellarBurgers


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description(
        'Проверка возможности перехода на страницу восстановления пароля по клику по кнопке «Восстановить пароль»')
    def test_open_password_recovery_page(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        login_page = BasePageStellarBurgers(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.wait_and_find_element(LoginPage.recover_password_link)
        login_page.element_click_new(LoginPage.recover_password_link)
        login_page.wait_and_find_element(PasswordRecoveryPage.recovery_button)
        assert login_page.get_url() == Urls.FORGOT_PASSWORD_PAGE

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description(
        'Проверка ввода почты и клика по кнопке «Восстановить» с переходом на страничку сброса пароля')
    def test_enter_email_and_click_recovery_button(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        login_page = BasePageStellarBurgers(driver)
        login_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        login_page.wait_and_find_element(PasswordRecoveryPage.email_field)
        login_page.element_click_new(PasswordRecoveryPage.email_field)
        login_page.send_keys_in_input(PasswordRecoveryPage.email_field , 'qwerty@mail.ru')
        login_page.element_click_new(PasswordRecoveryPage.recovery_button)
        login_page.wait_and_find_element(ResetPasswordPage.save_button)
        assert login_page.get_url() == Urls.RESET_PASSWORD_PAGE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    @allure.description(
        'Проверка, что кнопка глазок изменяет тип поля пароля и через тип скрывает пароль звездочками/отображает')
    def test_eye_icon(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]

        login_page = BasePageStellarBurgers(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.wait_and_find_element(LoginPage.password_field)
        login_page.element_click_new(LoginPage.password_field)
        login_page.send_keys_in_input(LoginPage.password_field, 'qwerty@mail.ru')
        password_field = login_page.get_element(LoginPage.password_field)
        #поле имеет тип password когда символы пароля закрыты (дефолт)
        assert password_field.get_attribute('type') == 'password'
        login_page.wait_and_find_element(LoginPage.eye_show_password_field)
        login_page.element_click_new(LoginPage.eye_show_password_field)
        password_field = login_page.get_element(LoginPage.password_field)
        #поле имеет тип text когда символы пароля открыты, проверим что состояние изменилось
        assert password_field.get_attribute('type') == 'text'
        #клик за пределом поля пароля, чтобы оно скрылось, например по полю почты
        login_page.wait_and_find_element(LoginPage.email_field)
        login_page.element_click_new(LoginPage.email_field)
        password_field = login_page.get_element(LoginPage.password_field)
        #проверяем что тип поля сменился на password, значит символы закрыты (снова дефолт)
        assert password_field.get_attribute('type') == 'password'



