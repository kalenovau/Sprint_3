from locators import TestLocatorsMainPage
from locators import TestLocatorsLoginPage
from locators import TestLocatorsProfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestLogin:

    def test_open_constructor_page_by_constructor_button(self): # Проверка перехода из ЛК в конструктор по кнопке "Конструктор"
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocatorsMainPage.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocatorsProfile.BUTTON_EXIT))
        driver.find_element(*TestLocatorsMainPage.CONSTRUCTOR).click()
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > h1").text == "Соберите бургер"
        driver.quit()

    def test_open_constructor_page_by_logo(self): # Проверка перехода из ЛК в конструктор по нажатию на логотип
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocatorsMainPage.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocatorsProfile.BUTTON_EXIT))
        driver.find_element(*TestLocatorsMainPage.LOGO).click()
        assert driver.find_element(By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > h1").text == "Соберите бургер"
        driver.quit()