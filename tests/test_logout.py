import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_logout(driver):
    """Тест выхода из аккаунта."""
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*MainPage.cabinet_button).click()
    driver.find_element(*LoginPage.email_input).send_keys("ivan@example.com")
    driver.find_element(*LoginPage.password_input).send_keys("123456")
    driver.find_element(*LoginPage.login_button).click()
    driver.find_element(*Cabinet.logout_button).click()
    # Проверка перехода на страницу входа
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(LoginPage.login_heading)
    )