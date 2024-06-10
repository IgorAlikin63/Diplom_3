from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import FeedPage
from pages.base_page import BasePageStellarBurgers
import allure

class FeedPageStellarBurgers(BasePageStellarBurgers):

    @allure.step("Ждем отображаение заказа")
    def wait_for_order_to_appear(self, order_number, timeout=30):
        #Ожидает появления номера заказа в списке заказов в работе
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: str(order_number) in self.get_in_work_list_numbers() and
                               'Все текущие заказы готовы!' not in self.get_in_work_list_numbers()
            )
        except TimeoutException:
            return False
        return True

    @allure.step("Получить номера из списка В работе")
    def get_in_work_list_numbers(self):
        #Возвращает текст элемента со списком заказов в работе
        return self.wait_and_find_element(FeedPage.in_work_list).text
