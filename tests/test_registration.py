# Проверка регистрации
from locators import TestLocatorsMainPage
from locators import TestLocatorsLoginPage
from locators import TestLocatorsRegistrationPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import string


email = random.choices(string.ascii_lowercase, k=5)

class TestRegistraion:
    def test_registration(self): #Проверка регистрации
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        driver.find_element(*TestLocatorsLoginPage.LINK_REGISTRATION).click()
        driver.find_element(By.NAME, "name").send_keys(random.choices(string.ascii_lowercase, k=5))
        driver.find_element(By.XPATH, '//label[.="Email"]/parent::*/input').send_keys(email)
        driver.find_element(By.XPATH, '//label[.="Email"]/parent::*/input').send_keys('@yandex.ru')
        driver.find_element(By.NAME, "Пароль").send_keys("SidSidSid1")
        driver.find_element(*TestLocatorsRegistrationPage.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        assert '/login' in driver.current_url
        driver.quit()

    def test_incorrect_password_error(self): #Проверка ошибки для некорректного пароля
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocatorsLoginPage.LINK_REGISTRATION))
        driver.find_element(*TestLocatorsLoginPage.LINK_REGISTRATION).click()
        driver.find_element(By.NAME, "name").send_keys("w")
        driver.find_element(By.XPATH, '//label[.="Email"]/parent::*/input').send_keys("www@yandex.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("w")
        driver.find_element(*TestLocatorsRegistrationPage.BUTTON_REGISTRATION).click()
        error = driver.find_element(*TestLocatorsRegistrationPage.INVALID_PASSWORD).text
        assert error == 'Некорректный пароль'
        driver.quit()
