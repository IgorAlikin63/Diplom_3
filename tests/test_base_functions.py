from urls import Urls
from locators import BasePageLocators
from conftest import driver
from pages.base_page import BasePageStellarBurgers
import allure
class TestBasePage:

    @allure.title('Перенаправление на конструктор')
    @allure.description('Проверка перенаправления на страницу конструктора по клику на конструктор')
    def test_constructor_link_redirect(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        base_page = BasePageStellarBurgers(driver)
        base_page.wait_and_find_element(BasePageLocators.feed_link)
        base_page.element_click_new(BasePageLocators.feed_link)
        base_page.wait_and_find_element(BasePageLocators.constructor_link)
        base_page.element_click_new(BasePageLocators.constructor_link)
        assert (base_page.get_url() == Urls.BASE_PAGE and
                base_page.wait_and_find_element(BasePageLocators.constructor_link).get_attribute('class') == 'AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo')

    @allure.title('Перенаправление на ленту заказов')
    @allure.description('Проверка перенаправления на страницу ленты заказов по клику на Лента заказов')
    def test_feed_link_redirect(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        base_page = BasePageStellarBurgers(driver)
        base_page.wait_and_find_element(BasePageLocators.feed_link)
        base_page.element_click_new(BasePageLocators.feed_link)
        assert (base_page.get_url() == Urls.FEED_LIST_PAGE and
                base_page.wait_and_find_element(BasePageLocators.feed_link).get_attribute(
                    'class') == 'AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo')

    @allure.title('Отображение карточки ингредиента по клику на него')
    @allure.description('Проверка отображения подробной карточки с информацией об ингредиенте по клику по нему')
    def test_ingredient_card_displayed_after_ingredient_click(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        base_page = BasePageStellarBurgers(driver)
        base_page.wait_and_find_element(BasePageLocators.crator_bun)
        base_page.element_click_new(BasePageLocators.crator_bun)
        base_page.wait_and_find_element(BasePageLocators.crator_bun_in_card_name)
        assert base_page.wait_and_find_element(BasePageLocators.crator_bun_in_card_name).text == 'Краторная булка N-200i'

    @allure.title('Закрытие информации об ингредиенте')
    @allure.description('Проверка закрытия карточки с подробной информацией об ингредиенте по клику на кнопку закрыть')
    def test_ingredient_card_can_be_closed(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        base_page = BasePageStellarBurgers(driver)
        base_page.wait_and_find_element(BasePageLocators.crator_bun)
        base_page.element_click_new(BasePageLocators.crator_bun)
        base_page.wait_and_find_element(BasePageLocators.close_button_in_card)
        base_page.element_click_new(BasePageLocators.close_button_in_card)
        base_page.unvisibility_of_element(BasePageLocators.close_button_in_card)
        assert not base_page.wait_and_find_element(BasePageLocators.close_button_in_card).is_displayed()

    @allure.title('Изменение счетчика ингредиента при добавлении его в конструктор')
    @allure.description('Проверка изменения счетчика ингредиента при добавлении этого ингредиента в конструктор бургера')
    def test_ingredient_counter_can_change(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        base_page = BasePageStellarBurgers(driver)
        base_page.drag_and_drop(BasePageLocators.crator_bun, BasePageLocators.burger_constructor_basket_section)
        assert base_page.get_element(BasePageLocators.crator_bun_counter).get_attribute('innerText') == '2'











