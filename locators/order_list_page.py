from selenium.webdriver.common.by import By

class OrderListPageLocators:

    TOP_ORDER_CARD_ON_FEED_LIST = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__1iNby')])[1]")
    TOP_INGREDIENT_IN_ORDER = (By.XPATH, "(//div[contains(@class,'Modal_imgBox__27yrH')])[1]")
    TOP_ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    ALL_TIME_ORDER_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]")
    TODAY_ORDER_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[2]")
    ORDER_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")