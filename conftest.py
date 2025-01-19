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
    driver.get(Urls.MAIN_PAGE) # Переход на главную страницу
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    """ Фикстура для входа в аккаунт. """
    driver.get(Urls.LOGIN)  # Переход на страницу входа

    driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(PersonalData.LOGIN)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(PersonalData.PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON_UNIVERSAL).click()

    # Явное ожидание появления кнопки на главной странице после авторизации
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))

    return driver
