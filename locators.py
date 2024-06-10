from selenium.webdriver.common.by import By


class BasePageLocators:

    login_button = (By.XPATH, '//button[contains(@class,"button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")][text()="Войти в аккаунт"]') #кнопка "Войти в аккаунт"
    make_burger_text = (By.XPATH, '//h1[contains(@class,"text text_type_main-large mb-5 mt-10")][text()="Соберите бургер"]') # текст Соберите бургер
    account_profile_link = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/account']") # линк Личный кабинет
    make_order_button = (By.XPATH, '//button[contains(@class,"button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")][text()="Оформить заказ"]') #кнопка оформить заказ
    constructor_link = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/']") # линк конструктор не активный
    feed_link = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/feed']") # линк лента заказов не активный
    crator_bun = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8') and @href='/ingredient/61c0c5a71d1f82001bdaaa6c']") #краторная булка в списке ингредиентов
    crator_bun_in_card_name = (By.XPATH, "//p[contains(@class, 'text text_type_main-medium mb-8')]") # краторная булка наименование в карточке булки
    crator_bun_counter = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']//p[contains(@class, 'counter_counter__num__3nue1')]") #счетчик краторной булки
    close_button_in_card = (By.XPATH, '//button[contains(@class,"Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")]') #кнопка закрыть модалку ингредиента
    burger_constructor_basket_section = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket__29Cd7 mt-25')]") #конструктор бургера
    close_button_for_created_order = (By.XPATH, '//button[contains(@class,"Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")]') #кнопка закрыть модалки нового заказа
    created_order_number = (By.XPATH, '//h2[contains(@class,"Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8")]') #номер нового заказа в модальном окне

class LoginPage:

    recover_password_link = (By.XPATH, '//a[contains(@class,"Auth_link__1fOlj")][text()="Восстановить пароль"]') #ссылка "Восстановить пароль"
    password_field = (By.XPATH, "//input[contains(@class, 'input__textfield') and @name='Пароль']")  # поле ввода пароль
    eye_show_password_field = (By.XPATH, '//div[contains(@class,"input__icon input__icon-action")]') #поле иконки глазок
    email_field = (By.XPATH, "//input[contains(@class, 'text') and contains(@class, 'input__textfield') and @name='name']")  # поле ввода почты
    login_button = (By.XPATH, '//button[contains(@class,"button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")][text()="Войти"]') #кнопка войти


class PasswordRecoveryPage:

    email_field = (By.XPATH, "//input[contains(@class, 'text input__textfield text_type_main-default')]") #поле ввода email
    recovery_button = (By.XPATH, '//button[contains(@class,"button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")][text()="Восстановить"]') #кнопка "Восстановить"

class ResetPasswordPage:

    save_button = (By.XPATH, '//button[contains(@class,"button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")][text()="Сохранить"]') #кнопка "Сохранить"


class AccountPage:

    orders_history_link = (By.XPATH, '//a[@href="/account/order-history"]') # линк история заказов
    logout_button = (By.XPATH, '//button[contains(@class,"Account_button__14Yp3 text text_type_main-medium text_color_inactive")][text()="Выход"]') #кнопка выход
    first_order_in_history = (By.XPATH, '//ul[contains(@class, "OrderHistory_profileList__374GU")]/li[contains(@class, "OrderHistory_listItem__2x95r")][1]/a[contains(@class, "OrderHistory_link__1iNby")]')
    last_order_in_history = (By.XPATH, '//ul[@class ="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]//li[last()]') #последний заказ в истории
    order_number = (By.XPATH, '//p[contains(@class, "text text_type_digits-default mb-10 mt-5")]') #номер заказа в карточке
    close_button_for_order_modal = (By.XPATH, '//button[contains(@class,"Account_button__14Yp3 text text_type_main-medium text_color_inactive")][text()="Выход"]') #кнопка выход в карточке заказа в истории


class FeedPage:

    orders_feed_header = (By.XPATH, '//h1[contains(@class,"text text_type_main-large mt-10 mb-5")][text()="Лента заказов"]') # заголовок ленты заказов "Лента заказов"
    orders_feed_list = (By.XPATH, '//ul[contains(@class,"OrderFeed_list__OLh59")]') # список лента заказов во вкладке лента заказов
    top_order_in_list_orders_feed_list = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem__2x95r")][1]') #самый свежий заказ в списке
    order_modal_close_button = (By.XPATH, '//button[contains(@class,"Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")]') #кнопка закрыть модалку заказа
    compound_text_in_order_modal = (By.XPATH, '//p[contains(@class,"text text_type_main-medium mb-8")][text()="Cостав"]') #текст Состав в заказе
    all_time_orders_counter = (By.XPATH, '//div[contains(@class,"undefined mb-15")]/p[contains(@class,"OrderFeed_number__2MbrQ text text_type_digits-large")]') #счетчик заказов за все время
    today_orders_counter = (By.XPATH,
                               '//div[p="Выполнено за сегодня:"]//following-sibling::p')  #счетчик заказов сегодня
    in_work_list = (By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady__1YFem ")]') #список в работе


