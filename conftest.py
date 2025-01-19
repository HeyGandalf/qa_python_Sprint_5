import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls
from helpers.data import PersonalData

@pytest.fixture
def driver():
    """ Фикстура для инициализации драйвера. """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10) # Ждать 10 секунд для всех операций, если элемент не найден.
    driver.get(Urls.main_page) # Переход на главную страницу
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    """ Фикстура для входа в аккаунт. """
    driver.get(Urls.login)  # Переход на страницу входа

    driver.find_element(*LoginPage.email_input).send_keys(PersonalData.login)
    driver.find_element(*LoginPage.password_input).send_keys(PersonalData.password)
    driver.find_element(*LoginPage.login_button_universal).click()

    # Явное ожидание появления кнопки на главной странице после авторизации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPage.order_button))

    return driver
