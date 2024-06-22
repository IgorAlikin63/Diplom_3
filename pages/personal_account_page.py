from pages.base_page import BasePage
from locators.personal_account_page import PersonalAccountLocators
import allure
from urls import Urls


class PersonalAccountPage(BasePage):
    @allure.step("Ввести почту в поле email")
    def set_email(self, email):
        input_email = self.wait_and_find_element(PersonalAccountLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step("Ввести пароль в поле 'Пароль'")
    def set_password(self, password):
        input_password = self.wait_and_find_element(PersonalAccountLocators.FIELD_PASSWORD)
        input_password.send_keys(password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        enter_button = self.wait_and_find_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.click_element(enter_button)

    @allure.step("Кликнуть по кнопке 'История заказов' в Личном кабинете")
    def click_order_history_button(self):
        order_history_btn = self.wait_and_find_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        self.click_element(order_history_btn)

    @allure.step("Кликнуть по кнопке 'Выход' в 'Личном Кабинете'")
    def click_logout_button(self):
        exit_btn = self.wait_and_find_element(PersonalAccountLocators.LOGOUT_BUTTON)
        self.click_element(exit_btn)

    @allure.step("Получить номер последнего заказа")
    def get_last_order_number(self):
        element = self.wait_and_find_element(PersonalAccountLocators.TOP_ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Кликнуть по кнопке 'Восстановить пароль'")
    def click_recovery_button(self):
        recovery_button = self.wait_and_find_element(PersonalAccountLocators.RECOVERY_PASSWORD_BUTTON)
        self.click_element(recovery_button)

    @allure.step("Проверить что открылcя Личный кабинет")
    def check_account_description_changes(self):
        element = self.wait_and_find_element(PersonalAccountLocators.DESCRIPTION_ACCOUNT_CHANGES_TEXT)
        return element.is_displayed()

    @allure.step("Дождаться пока откроется экран Авторизации")
    def find_login_page_title(self):
        element = self.wait_and_find_element(PersonalAccountLocators.TITLE_LOGIN_PAGE)
        return element.is_displayed()


    @allure.step("Проверяем текущий урл после действия со страницы personal_account_page")
    def check_current_url_after_action_in_personal_account_page(self):
        current_url = self.get_url()
        return current_url



