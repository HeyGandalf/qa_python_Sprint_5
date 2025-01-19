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

def test_login_from_main_page(driver):
    """Тест входа через главную страницу."""
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*MainPage.enter_cabinet_button).click()
    driver.find_element(*LoginPage.email_input).send_keys("ivan@example.com")
    driver.find_element(*LoginPage.password_input).send_keys("123456")
    driver.find_element(*LoginPage.login_button).click()
    # Проверка перехода в личный кабинет
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Cabinet.logout_button)
    )

def test_login_from_cabinet_button(driver):
    """Тест входа через кнопку 'Личный кабинет'."""
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*MainPage.cabinet_button).click()
    driver.find_element(*LoginPage.email_input).send_keys("ivan@example.com")
    driver.find_element(*LoginPage.password_input).send_keys("123456")
    driver.find_element(*LoginPage.login_button).click()
    # Проверка перехода в личный кабинет
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Cabinet.logout_button)
    )

def test_login_from_registration_form(driver):
    """Тест входа через форму регистрации."""
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*RegistrationPage.login_button).click()
    driver.find_element(*LoginPage.email_input).send_keys("ivan@example.com")
    driver.find_element(*LoginPage.password_input).send_keys("123456")
    driver.find_element(*LoginPage.login_button).click()
    # Проверка перехода в личный кабинет
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Cabinet.logout_button)
    )

def test_login_from_restore_password(driver):
    """Тест входа через форму восстановления пароля."""
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*RestorePassword.login_button).click()
    driver.find_element(*LoginPage.email_input).send_keys("ivan@example.com")
    driver.find_element(*LoginPage.password_input).send_keys("123456")
    driver.find_element(*LoginPage.login_button).click()
    # Проверка перехода в личный кабинет
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Cabinet.logout_button)
    )
