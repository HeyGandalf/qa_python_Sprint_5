from locators.locators import *

class TestStellarBurgersConstructor:

    def test_constructor_scroll_to_buns(self, login):
        """Проверка перехода к разделу Булки"""
        driver = login

        driver.find_element(*ConstructorTab.constructor_tab).click()
        driver.find_element(*ConstructorTab.filling_tab).click()
        driver.find_element(*ConstructorTab.buns_tab).click()

        buns_heading = driver.find_element(*ConstructorTab.buns_heading)

        assert buns_heading.text == 'Булки'
    def test_constructor_scroll_to_sauces(self, login):
        """Проверка перехода к разделу Соусы"""
        driver = login

        driver.find_element(*ConstructorTab.constructor_tab).click()
        driver.find_element(*ConstructorTab.sauces_tab).click()

        sauces_heading = driver.find_element(*ConstructorTab.sauces_heading)

        assert sauces_heading.text == 'Соусы'

    def test_constructor_scroll_to_filling(self, login):
        """Проверка перехода к разделу Начинки"""
        driver = login

        driver.find_element(*ConstructorTab.constructor_tab).click()
        driver.find_element(*ConstructorTab.filling_tab).click()

        filling_heading = driver.find_element(*ConstructorTab.filling_heading)

        assert filling_heading.text == 'Начинки'
