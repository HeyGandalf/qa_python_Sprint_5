from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *


class TestStellarBurgersConstructor:

    def test_constructor_scroll_to_buns(self, login):
        """Проверка перехода к разделу Булки"""
        driver = login

        # Прокручиваем страницу к элементу
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              driver.find_element(*ConstructorTab.CONSTRUCTOR_TAB))

        # Явное ожидание кликабельности и клик
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorTab.CONSTRUCTOR_TAB)).click()
        driver.find_element(*ConstructorTab.FILLING_TAB).click()
        driver.find_element(*ConstructorTab.BUNS_TAB).click()

        buns_heading = driver.find_element(*ConstructorTab.BUNS_HEADING)
        assert buns_heading.text == 'Булки'

    def test_constructor_scroll_to_sauces(self, login):
        """Проверка перехода к разделу Соусы"""
        driver = login

        # Прокручиваем страницу к элементу
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              driver.find_element(*ConstructorTab.CONSTRUCTOR_TAB))

        # Явное ожидание кликабельности и клик
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorTab.CONSTRUCTOR_TAB)).click()
        driver.find_element(*ConstructorTab.SAUCES_TAB).click()

        sauces_heading = driver.find_element(*ConstructorTab.SAUCES_HEADING)
        assert sauces_heading.text == 'Соусы'

    def test_constructor_scroll_to_filling(self, login):
        """Проверка перехода к разделу Начинки"""
        driver = login

        # Прокручиваем страницу к элементу
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              driver.find_element(*ConstructorTab.CONSTRUCTOR_TAB))

        # Явное ожидание кликабельности и клик
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorTab.CONSTRUCTOR_TAB)).click()
        driver.find_element(*ConstructorTab.FILLING_TAB).click()

        filling_heading = driver.find_element(*ConstructorTab.FILLING_HEADING)
        assert filling_heading.text == 'Начинки'
