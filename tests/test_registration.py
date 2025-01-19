import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_successful_registration(driver):
    """Тест успешной регистрации."""
    driver.get("https://stellar-burgers.example.com/register")
    driver.find_element(*RegistrationPage.name_input).send_keys("Иван Иванов")
    driver.find_element(*RegistrationPage.email_input).send_keys("ivan@example.com")
    driver.find_element(*RegistrationPage.password_input).send_keys("123456")
    driver.find_element(*RegistrationPage.register_button).click()
    # Проверка: пользователь перенаправлен на главную страницу
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(MainPage.logo)
    )

def test_registration_with_invalid_password(driver):
    """Тест ошибки при вводе некорректного пароля."""
    driver.get("https://stellar-burgers.example.com/register")
    driver.find_element(*RegistrationPage.name_input).send_keys("Иван Иванов")
    driver.find_element(*RegistrationPage.email_input).send_keys("ivan@example.com")
    driver.find_element(*RegistrationPage.password_input).send_keys("123")
    driver.find_element(*RegistrationPage.register_button).click()
    # Проверка ошибки
    error_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(RegistrationPage.error_message)
    ).text
    assert "Некорректный пароль" in error_message