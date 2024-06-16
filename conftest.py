import pytest
from selenium import webdriver
from urls import Urls

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    # Инициализация браузера
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(Urls.BASE_PAGE)
    yield browser
    browser.quit()

