from selenium.webdriver.common.by import By

class MainPage:
    """Локаторы для главной страницы"""
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers
    CABINET_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    ENTER_CABINET_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"

class ConstructorTab:
    """Локаторы для раздела конструктора"""
    CONSTRUCTOR_TAB = (By.XPATH, ".//p[text()='Конструктор']")  # Вкладка "Конструктор"
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::*")  # Вкладка "Соусы"
    SAUCES_HEADING = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")  # Заголовок "Соусы"
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::*")  # Вкладка "Булки"
    BUNS_HEADING = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")  # Заголовок "Булки"
    FILLING_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::*")  # Вкладка "Начинки"
    FILLING_HEADING = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")  # Заголовок "Начинки"

class RegistrationPage:
    """Локаторы для страницы регистрации"""
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # Поле ввода email на странице регистрации
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # Поле ввода пароля на странице регистрации
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")  # Ошибка для некорректного пароля
    LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка "Войти" на странице регистрации

class LoginPage:
    """Локаторы для страницы входа"""
    LOGIN_HEADING = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок Вход
    ELEMENT_WITH_LOGIN_TEXT = (By.XPATH, ".//*[text() = 'Вход']")  # Элемент с текстом вход
    LOGIN_TEXT_HREF = (By.XPATH, ".//a[text()='Войти']")  # Надпись Войти со ссылкой
    LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка "Войти" на странице входа
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # Поле ввода email на странице входа
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # Поле ввода пароля на странице входа
    LOGIN_BUTTON_UNIVERSAL = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти" использующаяся при разных вариантах входа

class RestorePasswordPage:
    LOGIN_TEXT_HREF = (By.XPATH, ".//a[text()='Войти']")  # Надпись Войти со ссылкой

class Cabinet:
    """Локаторы для страницы личного кабинета"""
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход"
    INFO_MESSAGE = (By.XPATH, ".//p[contains(text(),'В этом разделе')]")  # Пояснительная информация о разделе
    # Вкладка история заказов
    ORDER_HISTORY_TAB = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
