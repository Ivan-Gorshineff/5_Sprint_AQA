import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_chrome
from src.locators import BurgerLocators
from src.config import Config
from src.data import DataUser


class TestUserLogin:
    def test_login_into_account(self,driver_chrome):
        driver_chrome.get(Config.MAIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''Кликаем на кнопку "Войти в аккаунт'''
        get_into_account_btn = wait.until(EC.element_to_be_clickable(BurgerLocators.GET_INTO_ACCOUNT_BUTTON))
        get_into_account_btn.click()
        wait.until(EC.url_to_be(Config.LOGIN_PAGE_URL))
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email)
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        '''кликаем на кнопку "войти'''
        login_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_BUTTON))
        login_button.click()
        make_order_button = wait.until(EC.presence_of_element_located(BurgerLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed(), 'Кнопка "Оформить заказ" is not displayed'

    def test_login_personal_account(self,driver_chrome):
        driver_chrome.get(Config.MAIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''кликаем на кнопку "Личный кабинет'''
        personal_account_btn = wait.until(EC.element_to_be_clickable(BurgerLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_btn.click()
        wait.until(EC.url_to_be(Config.LOGIN_PAGE_URL))
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email)
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        '''кликаем на кнопку войти'''
        login_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_BUTTON))
        login_button.click()
        make_order_button = wait.until(EC.presence_of_element_located(BurgerLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed(), 'Кнопка "Оформить заказ" is not displayed'

    def test_login_form(self,driver_chrome):
        driver_chrome.get(Config.REGISTER_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''в форме регистрации кликаем на ссылку Войти'''
        login_form_btn = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_LINK))
        login_form_btn.click()
        wait.until(EC.url_to_be(Config.LOGIN_PAGE_URL))
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email)
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        login_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_BUTTON))
        login_button.click()
        make_order_button = wait.until(EC.presence_of_element_located(BurgerLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed(), 'Кнопка "Оформить заказ" is not displayed'

    def test_login_forgot(self,driver_chrome):
        driver_chrome.get(Config.FORGOT_PASSWORD_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''кликаем на ссылку "Войти'''
        login_form_btn = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_LINK))
        login_form_btn.click()
        wait.until(EC.url_to_be(Config.LOGIN_PAGE_URL))
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email)
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        login_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_BUTTON))
        login_button.click()
        make_order_button = wait.until(EC.presence_of_element_located(BurgerLocators.MAKE_ORDER_BUTTON))
        assert make_order_button.is_displayed(), 'Кнопка "Оформить заказ" is not displayed'