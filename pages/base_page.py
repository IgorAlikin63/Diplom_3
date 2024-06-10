from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure

class BasePageStellarBurgers:

    @allure.step("Инициировать драйвер")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть урл")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Подождать пока отобразится элемент")
    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def element_click(self, locator):
        #self.driver.find_element(*locator).click()
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step("Кликнуть на элемент по локатору")
    def element_click_new(self, locator):
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Получить текущий урл страницы")
    def get_url(self):
        return self.driver.current_url

    @allure.step("Получить элемент")
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Отправить значение в поле ввода")
    def send_keys_in_input(self, locator, text):
        input_element = self.wait_and_find_element(locator)
        input_element.send_keys(text)

    @allure.step("невидимость элемента, более не отображается")
    def unvisibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетащить элемент и опустить в конструктор")
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.wait_and_find_element(source_locator)
        target_element = self.wait_and_find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

    @allure.step("Получить номер только что созданного заказа")
    def get_new_order_number(self, locator):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(locator).text != '9999')
        new_order_number_element = self.wait_and_find_element(locator)
        new_order_number = new_order_number_element.text
        return int(new_order_number)




