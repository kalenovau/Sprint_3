from selenium.webdriver.common.by import By


class TestLocatorsMainPage:
    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")
    # Кнопка "Конструктор"
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    # Кнопка Лого
    LOGO = (By.XPATH, ".//a[@href='/']")
    # Кнопка "Булки"
    BUTTON_BUN = (By.XPATH, ".//div/div/*[text()='Булки']")
    # Кнопка "Соусы"
    BUTTON_SAUCES = (By.XPATH, ".//div/div/*[text()='Соусы']")
    # Кнопка "Начмнкм"
    BUTTON_FILLINGS = (By.XPATH, ".//div/div/*[text()='Начинки']")
    # Название раздела "Булки"
    TEXT_BUNS = (By.XPATH, ".//h2[text()='Булки']")
    # Название раздела "Соусы"
    TEXT_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")
    # Название раздела "Начинки"
    TEXT_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")

class TestLocatorsRegistrationPage:
    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # Сообщение "Некорректный пароль"
    INVALID_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")
    # Вход для уже зарегистрированного пользователя
    LINK_ALREADY_REGISTR = (By.XPATH, ".//a[@href='/login']")

class TestLocatorsLoginPage:
    # Поле ввода Email
    FIELD_EMAIL = (By.XPATH, "//label[.='Email']/parent::*/input")
    # Поле ввода пароля
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    # Кнопка "Войти" на странице авторизации
    BUTTON_ENTER = (By.XPATH, ".//*[text()='Войти']")
    # Ссылка "Восстановить пароль"
    LINK_RECOVERY_PASS = (By.XPATH, ".//a[@href='/forgot-password']")
    # Ссылка "Зарегистрироваться" на странице авторизации
    LINK_REGISTRATION = (By.XPATH, ".//a[@href='/register']")

class TestLocatorsProfile:
    # Кнопка "Выход"
    BUTTON_EXIT = (By.XPATH, './/*[contains(@class, "Account_button")]')
