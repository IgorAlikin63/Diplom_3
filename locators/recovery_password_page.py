from selenium.webdriver.common.by import By

class RecoveryPassPageLocators:

    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']")
    RECOVER_PASS_TITLE = (By.XPATH, "//h2[text()= 'Восстановление пароля']")
    FIELD_TYPE_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
    EYE_BUTTON = (By. XPATH, "//div[contains(@class,'input__icon input__icon-action')]")