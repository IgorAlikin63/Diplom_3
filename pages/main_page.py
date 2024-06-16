from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from urls import Urls
from locators.main_page import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Открыть в браузере страницу 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_PAGE)

    @allure.step("Кликнуть по кнопке 'Лента заказов' в шапке страницы")
    def click_feed_list_button(self):
        list_order_button = self.wait_and_find_element(MainPageLocators.LIST_ORDER_BUTTON)
        self.click_element(list_order_button)


    @allure.step("Кликнуть по 'Ингредиенту' в 'Конструкторе'")
    def click_ingredient_button(self):
        crator_bun = self.wait_and_find_element(MainPageLocators.CRATOR_BUN_INGREDIENT)
        self.click_element(crator_bun)

    @allure.step("Кликнуть по кнопке закрытия всплывающего окна")
    def close_ingredient_card(self):
        close_card_button = self.wait_and_find_element(MainPageLocators.CLOSE_CARD_BUTTON)
        self.click_element(close_card_button)
        self.wait_for_element_to_disappear(MainPageLocators.CLOSE_CARD_BUTTON)

    @allure.step("Кликнуть по кнопке закрытия окна нового заказа")
    def close_new_order_modal(self):
        close_card_button = self.wait_and_find_element(MainPageLocators.CLOSE_CARD_BUTTON)
        self.click_element(close_card_button)
        self.wait_for_element_to_disappear(MainPageLocators.CLOSE_CARD_BUTTON)

    @allure.step("Перетащить булку в конструктор бургера")
    def add_bun_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.CRATOR_BUN_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_CONSTRUCTOR)
        drag_and_drop(self.driver, source, target)

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_create_order_button(self):
        create_order_button = self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_element(create_order_button)

    @allure.step("Получить количество ингредиентов из счётчика")
    def get_count_ingredient(self):
        counter_element = self.wait_and_find_element(MainPageLocators.COUNTER)
        return counter_element.text

    @allure.step("Получить Email для авторизации из сгенерированных данных")
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step("Получить Password для авторизации из сгенерированных данных")
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step("Кликнуть по кнопке 'Личный кабинет'")
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.BUTTON_ACCOUNT)
        self.click_element(account_button)


    @allure.step("Получить номер оформленного заказа")
    def get_new_order_number(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER).text != '9999')
        new_order_number_element = self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER)
        new_order_number = new_order_number_element.text
        return int(new_order_number)

    @allure.step("Проверить что открылась карточка с информацией об ингредиенте")
    def check_ingredient_title_in_modal_window(self):
     #   if self.is_element_present(MainPageLocators.INGREDIENT_TITLE) == True:
        element = self.is_element_present(MainPageLocators.INGREDIENT_TITLE)
        if element and element.is_displayed():
            return True

    @allure.step("Проверить видимость кнопки закрытия модалки")
    def check_visibility_of_close_modal_button(self):
        element = self.is_element_present(MainPageLocators.CLOSE_CARD_BUTTON)
        if element and element.is_displayed():
            return True
        return False

    @allure.step("Дождаться пока откроется Главная страница")
    def find_main_page_title(self):
        return self.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE)

    @allure.step("Дождаться пока откроется окно с деталями заказа")
    def check_visibility_of_successfull_order_modal_text(self):
        element = self.wait_and_find_element(MainPageLocators.START_COOKING_TEXT)
        return element.is_displayed()

    @allure.step("Проверяем текущий урл после действия со страницы main_page")
    def check_current_url_after_action_in_main_page(self):
        current_url = self.get_url()
        return current_url



