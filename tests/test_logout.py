from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls

class TestStellarBurgersLogout:
    def test_logout_open_login_form(self, login):
        """"Тест выхода из аккаунта"""
        driver = login

        driver.find_element(*MainPage.cabinet_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(Cabinet.info_message))

        driver.find_element(*Cabinet.logout_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.login_button_universal))

        login_button = driver.find_element(*LoginPage.element_with_login_text)
        assert driver.current_url == Urls.login and login_button.text == 'Вход'
