from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls
from helpers.data import PersonalData

class TestStellarBurgersLogin:
    def test_login_valid_email_and_password_show_main_page(self, login):
        """ Тест ввода валидных данных при входе"""
        driver = login

        order_button = driver.find_element(*MainPage.ORDER_BUTTON)
        assert driver.current_url == Urls.MAIN_PAGE and order_button.text == 'Оформить заказ'

    def test_login_from_main_page_show_login_page(self, driver):
        """Тест входа через кноку 'Войти в аккаунт' на главной странице"""
        driver.find_element(*MainPage.ENTER_CABINET_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.LOGIN_HEADING))

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(PersonalData.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(PersonalData.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_UNIVERSAL).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.ORDER_BUTTON)
        assert driver.current_url == Urls.MAIN_PAGE and order_button.text == 'Оформить заказ'

    def test_login_from_cabinet_button_show_login_page(self, driver):
        """Тест входа через кнопку кнопку Личный кабинет"""
        driver.find_element(*MainPage.CABINET_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.LOGIN_HEADING))

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(PersonalData.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(PersonalData.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_UNIVERSAL).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.ORDER_BUTTON)
        assert driver.current_url == Urls.MAIN_PAGE and order_button.text == 'Оформить заказ'

    def test_login_from_registration_form(self, driver):
        """Тест входа через кнопку 'Войти' в форме регистрации"""
        driver.get(Urls.REGISTER)

        driver.find_element(*LoginPage.LOGIN_TEXT_HREF).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.LOGIN_HEADING))

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(PersonalData.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(PersonalData.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_UNIVERSAL).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.ORDER_BUTTON)
        assert driver.current_url == Urls.MAIN_PAGE and order_button.text == 'Оформить заказ'

    def test_login_from_restore_password(self, driver):
        """Тест входа через кнопку 'Войти' в форме восстановления пароля"""
        driver.get(Urls.FORGOT_PASSWORD)

        driver.find_element(*RestorePasswordPage.LOGIN_TEXT_HREF).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(LoginPage.LOGIN_HEADING))

        driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(PersonalData.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(PersonalData.PASSWORD)

        driver.find_element(*LoginPage.LOGIN_BUTTON_UNIVERSAL).click()
        WebDriverWait(driver, 8).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))

        order_button = driver.find_element(*MainPage.ORDER_BUTTON)
        assert driver.current_url == Urls.MAIN_PAGE and order_button.text == 'Оформить заказ'
