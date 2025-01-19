from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls
from helpers.data import PersonalData

class TestStellarBurgersLogin:
    def test_login_valid_email_and_password_show_main_page(self, login):
        """ Тест ввода валидных данных при входе"""
        driver = login

        order_button = driver.find_element(*MainPage.order_button)
        assert driver.current_url == Urls.main_page and order_button.text == 'Оформить заказ'

    def test_login_from_main_page_show_login_page(self, driver):
        """Тест входа через кноку 'Войти в аккаунт' на главной странице"""
        driver.find_element(*MainPage.enter_cabinet_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.login_heading))

        driver.find_element(*LoginPage.email_input).send_keys(PersonalData.login)
        driver.find_element(*LoginPage.password_input).send_keys(PersonalData.password)

        driver.find_element(*LoginPage.login_button_universal).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.order_button))

        order_button = driver.find_element(*MainPage.order_button)
        assert driver.current_url == Urls.main_page and order_button.text == 'Оформить заказ'

    def test_login_from_cabinet_button_show_login_page(self, driver):
        """Тест входа через кнопку кнопку Личный кабинет"""
        driver.find_element(*MainPage.cabinet_button).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.login_heading))

        driver.find_element(*LoginPage.email_input).send_keys(PersonalData.login)
        driver.find_element(*LoginPage.password_input).send_keys(PersonalData.password)

        driver.find_element(*LoginPage.login_button_universal).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.order_button))

        order_button = driver.find_element(*MainPage.order_button)
        assert driver.current_url == Urls.main_page and order_button.text == 'Оформить заказ'

    def test_login_from_registration_form(self, driver):
        """Тест входа через кнопку 'Войти' в форме регистрации"""
        driver.get(Urls.register)

        driver.find_element(*LoginPage.login_text_href).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.login_heading))

        driver.find_element(*LoginPage.email_input).send_keys(PersonalData.login)
        driver.find_element(*LoginPage.password_input).send_keys(PersonalData.password)

        driver.find_element(*LoginPage.login_button_universal).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.order_button))

        order_button = driver.find_element(*MainPage.order_button)
        assert driver.current_url == Urls.main_page and order_button.text == 'Оформить заказ'



    def test_login_from_restore_password(self, driver):
        """Тест входа через кнопку 'Войти' в форме восстановления пароля"""
        driver.get(Urls.forgot_password)

        driver.find_element(*RestorePasswordPage.login_text_href).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.login_heading))

        driver.find_element(*LoginPage.email_input).send_keys(PersonalData.login)
        driver.find_element(*LoginPage.password_input).send_keys(PersonalData.password)

        driver.find_element(*LoginPage.login_button_universal).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.order_button))

        order_button = driver.find_element(*MainPage.order_button)
        assert driver.current_url == Urls.main_page and order_button.text == 'Оформить заказ'
