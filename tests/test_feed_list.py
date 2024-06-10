from locators import BasePageLocators, AccountPage, FeedPage
from conftest import driver
import allure
from pages.base_page import BasePageStellarBurgers
from pages.login_page import LoginPageStellarBurgers
from pages.feed_list_page import FeedPageStellarBurgers
from urls import Urls


class TestFeedPage:

    @allure.title('Отображение модального окна заказа по клику по заказу')
    @allure.description(
        'Проверка отображения модалки заказа по клику по по этому заказу в списке заказов')
    def test_can_show_modal_order_window_by_click_on_order(self, driver):
        if isinstance(driver, tuple):
            driver = driver[0]
        base_page = BasePageStellarBurgers(driver)
        base_page.wait_and_find_element(BasePageLocators.feed_link)
        base_page.element_click_new(BasePageLocators.feed_link)
        base_page.wait_and_find_element(FeedPage.orders_feed_header)
        base_page.wait_and_find_element(FeedPage.orders_feed_list).is_displayed()
        base_page.wait_and_find_element(FeedPage.top_order_in_list_orders_feed_list)
        base_page.element_click(FeedPage.top_order_in_list_orders_feed_list)
        assert base_page.wait_and_find_element(FeedPage.compound_text_in_order_modal).is_displayed()

    @allure.title('Отображение заказа в ленте заказов')
    @allure.description(
        'Проверка отображения заказа в Лента заказов')
    def test_find_order_in_feed_list(self, driver):
        driver, user_data, user_session = driver
        page = LoginPageStellarBurgers(driver, user_data)
        page.wait_and_find_element(BasePageLocators.login_button)
        page.element_click_new(BasePageLocators.login_button)
        assert page.get_url() == Urls.LOGIN_PAGE
        page.login_with_fixture_data()
        assert page.wait_and_find_element(BasePageLocators.make_order_button).is_displayed()
        page.drag_and_drop(BasePageLocators.crator_bun, BasePageLocators.burger_constructor_basket_section)
        page.element_click_new(BasePageLocators.make_order_button)
        page.wait_and_find_element(BasePageLocators.close_button_for_created_order)
        page.element_click_new(BasePageLocators.close_button_for_created_order)
        page.element_click_new(BasePageLocators.account_profile_link)
        page.wait_and_find_element(AccountPage.orders_history_link)
        page.element_click_new(AccountPage.orders_history_link)
        page.wait_and_find_element(AccountPage.first_order_in_history)
        page.element_click_new(AccountPage.first_order_in_history)
        order_number = page.get_element(AccountPage.order_number).text
        page.element_click_new(AccountPage.close_button_for_order_modal)
        page.element_click(BasePageLocators.feed_link)
        feed_list = page.wait_and_find_element(FeedPage.orders_feed_list)
        feed_list_text = feed_list.text
        assert order_number in feed_list_text

    @allure.title('Изменение счетчика "Выполнено за все время" при добавлении заказа')
    @allure.description(
        'Проверка Изменение счетчика "Выполнено за все время" при добавлении нового заказа пользователем')
    def test_counter_all_orders_changes_with_new_order(self, driver):
        driver, user_data, user_session = driver
        page = LoginPageStellarBurgers(driver, user_data)
        page.wait_and_find_element(BasePageLocators.login_button)
        page.element_click(BasePageLocators.login_button)
        assert page.get_url() == Urls.LOGIN_PAGE
        page.login_with_fixture_data()
        assert page.wait_and_find_element(BasePageLocators.make_order_button).is_displayed()
        page.element_click(BasePageLocators.feed_link)
        page.wait_and_find_element(FeedPage.all_time_orders_counter)
        old_all_orders = page.get_element(FeedPage.all_time_orders_counter).text
        page.element_click(BasePageLocators.constructor_link)
        page.drag_and_drop(BasePageLocators.crator_bun, BasePageLocators.burger_constructor_basket_section)
        page.element_click(BasePageLocators.make_order_button)
        page.wait_and_find_element(BasePageLocators.close_button_for_created_order)
        page.element_click_new(BasePageLocators.close_button_for_created_order)
        page.element_click_new(BasePageLocators.feed_link)
        page.wait_and_find_element(FeedPage.all_time_orders_counter)
        new_all_orders = page.get_element(FeedPage.all_time_orders_counter).text
        assert old_all_orders < new_all_orders

    @allure.title('Изменение счетчика "Выполнено за сегодня" при добавлении заказа')
    @allure.description(
        'Проверка Изменение счетчика "Выполнено за сегодня" при добавлении нового заказа пользователем')
    def test_counter_today_orders_changes_with_new_order(self, driver):
        driver, user_data, user_session = driver
        page = LoginPageStellarBurgers(driver, user_data)
        page.wait_and_find_element(BasePageLocators.login_button)
        page.element_click(BasePageLocators.login_button)
        assert page.get_url() == Urls.LOGIN_PAGE
        page.login_with_fixture_data()
        assert page.wait_and_find_element(BasePageLocators.make_order_button).is_displayed()
        page.element_click(BasePageLocators.feed_link)
        page.wait_and_find_element(FeedPage.today_orders_counter)
        old_today_orders = page.get_element(FeedPage.today_orders_counter).text
        page.element_click(BasePageLocators.constructor_link)
        page.drag_and_drop(BasePageLocators.crator_bun, BasePageLocators.burger_constructor_basket_section)
        page.element_click(BasePageLocators.make_order_button)
        page.wait_and_find_element(BasePageLocators.close_button_for_created_order)
        page.element_click_new(BasePageLocators.close_button_for_created_order)
        page.element_click_new(BasePageLocators.feed_link)
        page.wait_and_find_element(FeedPage.today_orders_counter)
        new_today_orders = page.get_element(FeedPage.today_orders_counter).text
        assert old_today_orders < new_today_orders

    @allure.title('Новый заказ попадает в список "В работе"')
    @allure.description(
        'Проверка отображения нового заказа созданного пользователем в Ленте заказов - В работе')
    def test_new_order_number_in_in_work_list(self, driver):
        driver, user_data, user_session = driver
        page = LoginPageStellarBurgers(driver, user_data)
        feed_list_page = FeedPageStellarBurgers(driver)
        page.wait_and_find_element(BasePageLocators.login_button)
        page.element_click(BasePageLocators.login_button)
        assert page.get_url() == Urls.LOGIN_PAGE
        page.login_with_fixture_data()
        assert page.wait_and_find_element(BasePageLocators.make_order_button).is_displayed()
        page.drag_and_drop(BasePageLocators.crator_bun, BasePageLocators.burger_constructor_basket_section)
        page.element_click(BasePageLocators.make_order_button)
        page.wait_and_find_element(BasePageLocators.close_button_for_created_order)
        order_number = page.get_new_order_number(BasePageLocators.created_order_number)
        page.element_click_new(BasePageLocators.close_button_for_created_order)
        page.element_click_new(BasePageLocators.feed_link)
        assert feed_list_page.wait_for_order_to_appear(order_number)



