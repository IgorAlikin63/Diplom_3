from selenium.webdriver.common.by import By
class MainPageLocators:

    BUTTON_ACCOUNT = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/account']")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    LIST_ORDER_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_CARD_BUTTON = (By.XPATH, "//button[@type='button']")
    BURGER_CONSTRUCTOR = (By.XPATH, "//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    CRATOR_BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')])[2]")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    START_COOKING_TEXT = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    COUNTER = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[2]")
    NUMBER_NEW_ORDER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")