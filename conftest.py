import pytest
from selenium import webdriver
from user_api import UserApi, UserSession
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

    # Создание нового пользователя через API
    user_data = UserApi.register_new_user_and_return_email_password()
    assert user_data, "Не удалось создать пользователя"

    # Авторизация пользователя и получение accessToken
    user_session = UserSession()
    user_session = UserApi.login_user(user_session, user_data['email'], user_data['password'])
    assert user_session.accessToken, "Не удалось авторизовать пользователя"

    # Предоставление данных браузера и пользователя для теста
    yield browser, user_data, user_session

    # Закрытие браузера
    browser.quit()

    # Удаление пользователя после завершения теста
    delete_response = UserApi.delete_user(user_session)
    assert delete_response['success'], "Не удалось удалить пользователя"