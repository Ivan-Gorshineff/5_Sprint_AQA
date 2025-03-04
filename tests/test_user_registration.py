import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_chrome
from src.locators import BurgerLocators
from src.config import Config
from src.data import DataUser

class TestUserRegistration:

    def test_registration(self, driver_chrome):
        driver_chrome.get(Config.REGISTER_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''вводим имя для регистрации'''
        name_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_NAME_INPUT))
        name_input.send_keys(DataUser.test_name)
        '''вводим почту для регистрации'''
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email_random)
        '''вводим пароль для регистрации'''
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        '''кликаем на Зарегистрироваться'''
        registration_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_REGISTRATION_BUTTON))
        registration_button.click()
        login_button = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_LOGIN_BUTTON))
        assert login_button.is_displayed() is True, 'Button is not displayed'

    def test_incorrect_registration(self, driver_chrome):
        driver_chrome.get(Config.REGISTER_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        name_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_NAME_INPUT))
        name_input.send_keys(DataUser.test_name)
        incorrect_email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        incorrect_email_input.send_keys('4r5')
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys('45')
        registration_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_REGISTRATION_BUTTON))
        registration_button.click()
        error_registration = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_INCORRECT_PASSWORD))
        assert error_registration.is_displayed()
