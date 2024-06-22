from pages.base_page import BasePage
from locators.order_list_page import OrderListPageLocators
import allure


class OrderListPage(BasePage):

    @allure.step("Открыть окно с деталями заказа кликом по карточке заказа")
    def click_top_order_card(self):
        order_card = self.wait_and_find_element(OrderListPageLocators.TOP_ORDER_CARD_ON_FEED_LIST)
        self.click_element(order_card)

    @allure.step("Получить номер последнего заказа")
    def get_top_order_number(self):
        element = self.wait_and_find_element(OrderListPageLocators.TOP_ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Получить значение счётчика 'Выполнено за все время'")
    def get_all_time_orders_counter(self):
        number = self.wait_and_find_element(OrderListPageLocators.ALL_TIME_ORDER_COUNTER)
        return int(number.text)

    @allure.step("Кликнуть по кнопке 'Конструктор'")
    def click_constructor_button(self):
        constructor_button = self.wait_and_find_element(OrderListPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(constructor_button)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        number = self.wait_and_find_element(OrderListPageLocators.TODAY_ORDER_COUNTER)
        return int(number.text)

    @allure.step("Получить номер заказа в разделе 'В работе'")
    def get_order_in_works_number(self):
        number_in_works = self.wait_and_find_element(OrderListPageLocators.ORDER_IN_WORK)
        return int(number_in_works.text)

    @allure.step("Проверить что открылось окно с деталями заказа, проверяем отображение элемента какого-либо ингрединта в списке")
    def check_open_window_with_order_details(self):
        return self.is_element_present(OrderListPageLocators.TOP_INGREDIENT_IN_ORDER)


    @allure.step("Проверяем текущий урл после действия со страницы order_list_page")
    def check_current_url_after_action_in_order(self):
        current_url = self.get_url()
        return current_url

