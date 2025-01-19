import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls
from helpers.data import ValidData

class TestStellarBurgersRegistration:
    def test_successful_registration_valid_email_and_password(self, driver):
        """Тест успешной регистрации"""
        driver.get(Urls.REGISTER)

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(ValidData.USER_NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(ValidData.LOGIN)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(ValidData.PASSWORD)

        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.ELEMENT_WITH_LOGIN_TEXT))

        login_button = driver.find_element(*LoginPage.ELEMENT_WITH_LOGIN_TEXT)
        assert driver.current_url == Urls.LOGIN and login_button.text == 'Вход'

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_with_invalid_password_error_message(self, driver, password):
        """Тест ошибки при вводе некорректного пароля"""
        driver.get(Urls.REGISTER)

        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(ValidData.USER_NAME)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(ValidData.LOGIN)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(RegistrationPage.ERROR_MESSAGE))
        error_message = driver.find_element(*RegistrationPage.ERROR_MESSAGE)

        assert error_message.text == 'Некорректный пароль'
