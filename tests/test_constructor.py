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

def test_constructor_tabs(driver):
    """Тест переходов к разделам конструктора."""
    driver.get("https://stellar-burgers.example.com")
    driver.find_element(*Constructor.buns_tab).click()
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Constructor.buns_heading)
    )
    driver.find_element(*Constructor.sauces_tab).click()
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Constructor.sauces_heading)
    )
    driver.find_element(*Constructor.filling_tab).click()
    assert WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(Constructor.filling_heading)
    )
