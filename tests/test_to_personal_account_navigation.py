import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_chrome
from src.locators import BurgerLocators
from src.config import Config
from src.data import DataUser


class TestPersonalAccountNavigation:
    def test_personal_account_nav(self, driver_chrome):
        driver_chrome.get(Config.LOGIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        """заполнение полей и клик"""
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email)
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        login_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_BUTTON))
        login_button.click()
        """кликаем на кнопку Личный Кабинет"""
        wait.until(EC.url_to_be(Config.MAIN_PAGE_URL))
        personal_account_btn = wait.until(EC.element_to_be_clickable(BurgerLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_btn.click()
        """переход в Личный Кабинет"""
        wait.until(EC.url_to_be(Config.PROFILE_PAGE_URL))
        logout_button = wait.until(EC.presence_of_element_located(BurgerLocators.LOGOUT_BUTTON))
        assert logout_button.is_displayed(), 'Кнопка "Выйти "is not displayed'

