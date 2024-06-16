from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage
import allure
from user_api import UserApi



class TestFeedPage:

    @allure.title('Отображение модального окна заказа по клику по заказу')
    @allure.description(
        'Проверка отображения модалки заказа по клику по по этому заказу в списке заказов')
    def test_can_show_modal_order_window_by_click_on_order(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_feed_list_button()
        order_list_page = OrderListPage(driver)
        order_list_page.click_top_order_card()
        assert order_list_page.check_open_window_with_order_details()

    @allure.title('Отображение заказа в ленте заказов')
    @allure.description(
        'Проверка отображения заказа в Лента заказов')
    def test_find_order_in_feed_list(self, driver):
        user_data = UserApi.generate_user_data() #Заводим нового юзера со случайными данными
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver) #Авторизуем нового юзера с этими данными
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title() #Провевеяем, что после всех манипуляций вернулись на главную страницу
        main_page.add_bun_in_order()  #Создаём объект какого то бургера через конструктор
        main_page.click_create_order_button()
        main_page.close_new_order_modal()
        main_page.find_main_page_title() #Переходим на экран "История заказов" и получаем номер последнего заказа
        main_page.click_account_button()
        personal_account_page.click_order_history_button()
        order_number = personal_account_page.get_last_order_number()
        main_page.click_feed_list_button() #Переходим на экран "Лента заказов" c главной страницы и получаем номер последнего заказа
        order_list_page = OrderListPage(driver)
        order_number_in_list = order_list_page.get_top_order_number()
        assert order_number == order_number_in_list
        access_token = UserApi.get_access_token(user_response)  #Удаляем созданного пользователя
        UserApi.delete_user(access_token)

    @allure.title('Изменение счетчика "Выполнено за все время" при добавлении заказа')
    @allure.description(
        'Проверка Изменение счетчика "Выполнено за все время" при добавлении нового заказа пользователем')
    def test_counter_all_orders_changes_with_new_order(self, driver):
        user_data = UserApi.generate_user_data()  # Заводим нового юзера со случайными данными
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)  #Авторизуем нового юзера с этими данными
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title()  # Провевеяем, что после всех манипуляций вернулись на главную страницу
        main_page.click_feed_list_button()
        order_list_page = OrderListPage(driver) # Получаем значение счётчика заказов на странице "Лента заказов"
        counter_all_time_orders = order_list_page.get_all_time_orders_counter()
        order_list_page.click_constructor_button() # Переходим в конструктор и создаём заказ
        main_page.add_bun_in_order()  # Создаём объект какого то бургера через конструктор
        main_page.click_create_order_button()
        main_page.close_new_order_modal()
        main_page.click_feed_list_button() # Переходим на экран "Лента заказов" и получаем значение счётчика всех заказов
        counter_all_time_orders_new = order_list_page.get_all_time_orders_counter()
        assert counter_all_time_orders_new > counter_all_time_orders
        access_token = UserApi.get_access_token(user_response)  # Удаляем созданного пользователя
        UserApi.delete_user(access_token)

    @allure.title('Изменение счетчика "Выполнено за сегодня" при добавлении заказа')
    @allure.description(
        'Проверка Изменение счетчика "Выполнено за сегодня" при добавлении нового заказа пользователем')
    def test_counter_today_orders_changes_with_new_order(self, driver):
        user_data = UserApi.generate_user_data()  # Заводим нового юзера со случайными данными
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)  # Авторизуем нового юзера с этими данными
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title()  # Провевеяем, что после всех манипуляций вернулись на главную страницу
        main_page.click_feed_list_button()
        order_list_page = OrderListPage(driver) # Получаем значение счётчика заказов на странице "Лента заказов"
        counter_today_orders = order_list_page.get_today_orders_counter()
        order_list_page.click_constructor_button()# Переходим в конструктор и создаём заказ
        main_page.add_bun_in_order()  # Создаём объект какого то бургера через конструктор
        main_page.click_create_order_button()
        main_page.close_new_order_modal()
        main_page.click_feed_list_button() # Переходим на экран "Лента заказов" и получаем значение счётчика всех заказов
        counter_today_orders_new = order_list_page.get_today_orders_counter()
        assert counter_today_orders_new > counter_today_orders
        access_token = UserApi.get_access_token(user_response)  # Удаляем созданного пользователя
        UserApi.delete_user(access_token)

    @allure.title('Новый заказ попадает в список "В работе"')
    @allure.description(
        'Проверка отображения нового заказа созданного пользователем в Ленте заказов - В работе')
    def test_new_order_number_in_in_work_list(self, driver):
        user_data = UserApi.generate_user_data()  # Заводим нового юзера со случайными данными
        user_response = UserApi.register_user(user_data)
        main_page = MainPage(driver)
        main_page.open()
        email = main_page.get_user_email(user_data)
        password = main_page.get_user_password(user_data)
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)  # Авторизуем нового юзера с этими данными
        personal_account_page.set_email(email)
        personal_account_page.set_password(password)
        personal_account_page.click_login_button()
        main_page.find_main_page_title()  # Провевеяем, что после всех манипуляций вернулись на главную страницу
        main_page.add_bun_in_order()  # Создаём объект какого то бургера через конструктор
        main_page.click_create_order_button()
        new_order_number = main_page.get_new_order_number()
        main_page.close_new_order_modal()
        main_page.click_feed_list_button() # Переходим на экран "Лента заказов" и получаем номер заказа, попавшего столбец "В работе"
        order_list_page = OrderListPage(driver)
        new_order_number_in_order_list = order_list_page.get_order_in_works_number()
        assert new_order_number_in_order_list == new_order_number
        access_token = UserApi.get_access_token(user_response)  # Удаляем созданного пользователя
        UserApi.delete_user(access_token)



