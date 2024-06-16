from user_api import UserApi
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage
import allure
from urls import Urls

class TestBasePage:

    @allure.title('Перенаправление на конструктор')
    @allure.description('Проверка перенаправления на страницу конструктора по клику на Конструктор')
    def test_constructor_link_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_feed_list_button
        order_list_page = OrderListPage(driver)
        order_list_page.click_constructor_button()
        current_url = order_list_page.check_current_url_after_action_in_order()
        assert current_url == Urls.BASE_PAGE

    @allure.title('Перенаправление на ленту заказов')
    @allure.description('Проверка перенаправления на страницу ленты заказов по клику на Лента заказов')
    def test_feed_link_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_feed_list_button()
        current_url = main_page.check_current_url_after_action_in_main_page()
        assert current_url == Urls.FEED_LIST_PAGE

    @allure.title('Отображение карточки ингредиента по клику на него')
    @allure.description('Проверка отображения подробной карточки с информацией об ингредиенте по клику по нему')
    def test_ingredient_card_displayed_after_ingredient_click(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        assert main_page.check_ingredient_title_in_modal_window()

    @allure.title('Закрытие информации об ингредиенте')
    @allure.description('Проверка закрытия карточки с подробной информацией об ингредиенте по клику на кнопку закрыть')
    def test_ingredient_card_can_be_closed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient_button()
        main_page.close_ingredient_card()
        assert not main_page.check_visibility_of_close_modal_button()

    @allure.title('Изменение счетчика ингредиента при добавлении его в конструктор')
    @allure.description('Проверка изменения счетчика ингредиента при добавлении этого ингредиента в конструктор бургера')
    def test_ingredient_counter_can_change(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_bun_in_order()
        assert main_page.get_count_ingredient() == '2'

    @allure.title('Авторизованный пользователь может сделать заказ')
    @allure.description(
        'Проверка возможности авторизованного пользователя оформить заказ, отображение кнопки Оформить заказ')
    def test_authorized_user_can_do_order(self, driver):
        user_data = UserApi.generate_user_data()
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title()
        main_page.add_bun_in_order()
        main_page.click_create_order_button()
        assert main_page.check_visibility_of_successfull_order_modal_text()
        access_token = UserApi.get_access_token(user_response)
        UserApi.delete_user(access_token)













