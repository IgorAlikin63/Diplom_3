from urls import Urls
from conftest import driver
from pages.main_page import MainPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.personal_account_page import PersonalAccountPage
import allure
from data import UserData


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description(
        'Проверка возможности перехода на страницу восстановления пароля по клику по кнопке «Восстановить пароль»')
    def test_open_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        current_url = recovery_page.check_current_url_after_action_in_recovery_password_page()
        assert current_url == Urls.FORGOT_PASSWORD_PAGE

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description(
        'Проверка ввода почты и клика по кнопке «Восстановить» с переходом на страничку сброса пароля')
    def test_enter_email_and_click_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_password_recovery_button()
        recovery_page.check_recovery_pass_title_is_shown()
        current_url = recovery_page.check_current_url_is_reset_password_page()
        assert current_url == Urls.RESET_PASSWORD_PAGE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    @allure.description(
        'Проверка, что кнопка глазок изменяет тип поля пароля и через тип скрывает пароль звездочками/отображает')
    def test_eye_icon(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_password_recovery_button()
        recovery_page.set_password_in_password_field_in_reset_page(UserData.NEW_USER_PASSWORD)
        old_field_type = recovery_page.get_password_input_type()
        recovery_page.click_show_eye_button()
        new_field_type = recovery_page.get_password_input_type()
        assert old_field_type != new_field_type




