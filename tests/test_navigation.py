from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from helpers.urls import Urls
from selenium.webdriver.common.by import By
class TestStellarBurgersNavigation:
    def test_click_cabinet_button_open_cabinet(self, login):
        """Тест перехода в личный кабинет по клику на 'Личный кабинет'"""
        driver = login

        driver.find_element(*MainPage.cabinet_button).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Cabinet.info_message))
        profile = driver.find_element(*Cabinet.order_history_tab)
        assert Urls.profile == driver.current_url and profile.text == 'История заказов'
    def test_click_constructor_button_open_constructor_tab(self, login):
        """Тест перехода из личного кабинета в Конструктор по клику на кнопку 'Конструктор' """
        driver = login

        driver.find_element(*MainPage.cabinet_button).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Cabinet.info_message))
        driver.find_element(*ConstructorTab.constructor_tab).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'
    def test_click_logo_open_constructor_tab(self, login):
        """Тест перехода из личного кабинета в Конструктор по клику на логотип Stellar Burgers """
        driver = login

        driver.find_element(*MainPage.cabinet_button).click()

        WebDriverWait(driver,5).until(EC.presence_of_element_located(Cabinet.info_message))
        driver.find_element(*MainPage.logo).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'
