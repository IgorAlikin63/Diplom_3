from selenium.webdriver.common.by import By

class PersonalAccountLocators:

    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'][1]")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    DESCRIPTION_ACCOUNT_CHANGES_TEXT = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[text()='Вход']")
    TOP_ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
