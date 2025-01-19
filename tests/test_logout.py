from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls

class TestStellarBurgersLogout:
    def test_logout_open_login_form(self, login):
        """"Тест выхода из аккаунта"""
        driver = login

        driver.find_element(*MainPage.CABINET_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(Cabinet.INFO_MESSAGE))

        driver.find_element(*Cabinet.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON_UNIVERSAL))

        login_button = driver.find_element(*LoginPage.ELEMENT_WITH_LOGIN_TEXT)
        assert driver.current_url == Urls.LOGIN and login_button.text == 'Вход'
