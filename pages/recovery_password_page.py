from pages.base_page import BasePage
from locators.recovery_password_page import RecoveryPassPageLocators
import allure
from urls import Urls

class RecoveryPasswordPage(BasePage):
    @allure.step("Ввести почту в поле email")
    def set_email(self, email):
        input_email = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_EMAIL)
        input_email.send_keys(email)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_password_recovery_button(self):
        recovery_button = self.wait_and_find_element(RecoveryPassPageLocators.PASSWORD_RECOVERY_BUTTON)
        self.click_element(recovery_button)

    @allure.step("Ввести пароль на странице сброса")
    def set_password_in_password_field_in_reset_page(self, password):
        input_password = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_TYPE_PASSWORD)
        input_password.send_keys(password)

    @allure.step("Кликнуть по кнопке 'Глаз' отображения скрытого пароля")
    def click_show_eye_button(self):
        eye_button = self.wait_and_find_element(RecoveryPassPageLocators.EYE_BUTTON)
        self.click_element(eye_button)

    @allure.step('Получить тип поля пароля')
    def get_password_input_type(self):
        input_password = self.wait_and_find_element(RecoveryPassPageLocators.FIELD_TYPE_PASSWORD)
        return input_password.get_attribute("type") == "text"

    @allure.step("Проверить, что открылся экран восстановления пароля после ввода пароля")
    def check_recovery_pass_title_is_shown(self):
        element = self.wait_and_find_element(RecoveryPassPageLocators.RECOVER_PASS_TITLE)
        return element.is_displayed()

    @allure.step("Проверяем текущий урл после действия со страницы recovery_password_page")
    def check_current_url_after_action_in_recovery_password_page(self):
        current_url = self.get_url()
        return current_url

    @allure.step("Проверяем текущий урл после действия со страницы recovery_password_page с ожиданием загрузки")
    def check_current_url_is_reset_password_page(self):
        return self.wait_for_url_to_be(Urls.RESET_PASSWORD_PAGE)
