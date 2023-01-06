from locators import TestLocatorsMainPage
from locators import TestLocatorsLoginPage
from locators import TestLocatorsProfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_change_section_bun_to_sauces(self):  # Проверка перехода от раздела Булки к разделу Соусы
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocatorsMainPage.BUTTON_SAUCES).click()
        assert driver.find_element(*TestLocatorsMainPage.TEXT_SAUCES)
        driver.quit()

    def test_change_section_sauces_to_fillings(self):  # Проверка перехода от раздела Соусы к разделу Начинки
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocatorsMainPage.BUTTON_SAUCES).click()
        driver.find_element(*TestLocatorsMainPage.BUTTON_FILLINGS).click()
        assert driver.find_element(*TestLocatorsMainPage.TEXT_FILLINGS)
        driver.quit()

    def test_change_section_fillings_to_buns(self):  # Проверка перехода от раздела Начинки к разделу Булки
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocatorsMainPage.BUTTON_FILLINGS).click()
        driver.find_element(*TestLocatorsMainPage.BUTTON_BUN).click()
        assert driver.find_element(*TestLocatorsMainPage.TEXT_BUNS)
        driver.quit()
