import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_cabinet_navigation(driver):
    """Тест перехода по клику на 'Личный кабинет'."""
    driver.get("https://stellar-burgers.example.com")
    driver.find_element(*MainPage.cabinet_button).click()
    # Проверка перехода на страницу входа
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(LoginPage.login_heading)
    )

def test_constructor_navigation(driver):
    """Тест перехода из личного кабинета в конструктор."""
    driver.get("https://stellar-burgers.example.com")
    driver.find_element(*MainPage.logo).click()
    # Проверка, что пользователь попал в конструктор
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Constructor.constructor_tab)
    )
