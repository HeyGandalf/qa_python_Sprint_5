import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls
from helpers.data import ValidData

class TestStellarBurgersRegistration:
    def test_successful_registration_valid_email_and_password(self, driver):
        """Тест успешной регистрации"""
        driver.get(Urls.register)

        driver.find_element(*RegistrationPage.name_input).send_keys(ValidData.user_name)
        driver.find_element(*RegistrationPage.email_input).send_keys(ValidData.login)
        driver.find_element(*RegistrationPage.password_input).send_keys(ValidData.password)

        driver.find_element(*RegistrationPage.register_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.element_with_login_text))

        login_button = driver.find_element(*LoginPage.element_with_login_text)
        assert driver.current_url == Urls.login and login_button.text == 'Вход'

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_with_invalid_password_error_message(self, driver, password):
        """Тест ошибки при вводе некорректного пароля"""
        driver.get(Urls.register)

        driver.find_element(*RegistrationPage.name_input).send_keys(ValidData.user_name)
        driver.find_element(*RegistrationPage.email_input).send_keys(ValidData.login)
        driver.find_element(*RegistrationPage.password_input).send_keys(password)

        driver.find_element(*RegistrationPage.register_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(RegistrationPage.error_message))
        error_message = driver.find_element(*RegistrationPage.error_message)

        assert error_message.text == 'Некорректный пароль'
