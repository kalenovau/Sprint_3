from locators import TestLocatorsMainPage
from locators import TestLocatorsLoginPage
from locators import TestLocatorsRegistrationPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestLogin:

    def test_login_button_main_page(self): # Проверка входа по кнопке «Войти в аккаунт» на главной
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        #Кликнул по кнопке "Войти в аккаунт"
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        #Дождался загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        #Заполняю поля
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        #Нажал кнопку "Войти"
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        #Дождался загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/main/section[2]/div/button")))
        #Проверил что авторизован
        assert driver.find_element(By.XPATH, ".//div/main/section[2]/div/button").text == "Оформить заказ"
        driver.quit()

    def test_login_by_personal_area(self): # Проверка входа по кнопке «Личный кабинет»
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        #Кликнул по кнопке "Личнй кабиент"
        driver.find_element(*TestLocatorsMainPage.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocatorsLoginPage.LINK_REGISTRATION))
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        time.sleep(4)
        assert driver.find_element(*TestLocatorsMainPage.LOGO).is_displayed()
        driver.quit()

    def test_login_on_registration_page(self): # Проверка входа через кнопку в форме регистрации
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        driver.find_element(*TestLocatorsLoginPage.LINK_REGISTRATION).click()
        driver.find_element(*TestLocatorsRegistrationPage.LINK_ALREADY_REGISTR).click()
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/main/section[2]/div/button")))
        assert driver.find_element(By.XPATH, ".//div/main/section[2]/div/button").text == "Оформить заказ"
        driver.quit()

    def test_login_on_forgot_password_page(self): # Проверка входа через кнопку восстановления пароля
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        driver.find_element(*TestLocatorsLoginPage.LINK_RECOVERY_PASS).click()
        driver.find_element(By.XPATH, ".//div/main/div/div/p/a").click()
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/main/section[2]/div/button")))
        assert driver.find_element(By.XPATH, ".//div/main/section[2]/div/button").text == "Оформить заказ"
        driver.quit()
