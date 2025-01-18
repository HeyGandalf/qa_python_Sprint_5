from selenium.webdriver.common.by import By
class MainPage:
    """Локаторы для главной страницы"""
    logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # Логотип Stellar Burgers
    cabinet_button = (By.XPATH, ".//p[text()='Личный Кабинет']") # Кнопка "Личный кабинет"
    enter_cabinet_button = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    order_button = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"

class Constructor:
    """Локаторы для раздела конструктора"""
    constructor_tab = (By.XPATH, ".//p[text()='Конструктор']") # Вкладка "Конструктор"
    sauces_tab = (By.XPATH, ".//span[text()='Соусы']/parent::*") # Вкладка "Соусы"
    sauces_heading = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']") # Заголовок "Соусы"
    buns_tab = (By.XPATH, ".//span[text()='Булки']/parent::*") # Вкладка "Булки"
    buns_heading = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']") # Заголовок "Булки"
    filling_tab = (By.XPATH, ".//span[text()='Начинки']/parent::*") # Вкладка "Начинки"
    filling_heading = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']") # Заголовок "Начинки"

class RegistrationPage:
    """Локаторы для страницы регистрации"""
    name_input = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']") # Поле ввода имени
    email_input = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']") # Поле ввода email на странице регистрации
    password_input = (By.XPATH, ".//input[@type='password' and @name='Пароль']") # Поле ввода пароля на странице регистрации
    register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    error_message = (By.XPATH, ".//p[contains(@class, 'input__error')]") # Ошибка для некорректного пароля
    login_button = (By.CLASS_NAME, "Auth_link__1fOlj") # Кнопка "Войти" на странице регистрации

class LoginPage:
    """Локаторы для страницы входа"""
    login_heading = (By.XPATH, ".//h2[text()='Вход']") # Заголовок Вход
    email_input = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']") # Поле ввода email на странице входа
    password_input = (By.XPATH, ".//input[@type='password' and @name='Пароль']") # Поле ввода пароля на странице входа
    login_button = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти" на странице входа

class RestorePassword:
    """Локаторы для страницы восстановление пароля"""
    login_button = (By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")  # Кнопка "Войти" на странице Восстановление пароля

class Cabinet:
    """Локаторы для страницы личного кабинета"""
    logout_button = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выйти"
