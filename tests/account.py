from locators import TestLocatorsMainPage
from locators import TestLocatorsLoginPage
from locators import TestLocatorsProfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestLogin:

    def test_open_account_page(self):  # Проверка входа в личный кабинет
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocatorsMainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
        driver.find_element(*TestLocatorsLoginPage.FIELD_EMAIL).send_keys("Александр_Каленов_05_000@yandex.ru")
        driver.find_element(*TestLocatorsLoginPage.FIELD_PASSWORD).send_keys("Александр")
        driver.find_element(*TestLocatorsLoginPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div/main/section[2]/div/button")))
        driver.find_element(*TestLocatorsMainPage.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocatorsProfile.BUTTON_EXIT))
        assert driver.find_element(By.XPATH, ".//div/main/div/nav/p").text == "В этом разделе вы можете изменить свои персональные данные"
        driver.quit()
