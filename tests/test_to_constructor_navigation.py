from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_chrome
from src.locators import BurgerLocators
from src.config import Config
from src.data import DataUser


class TestConstructorNavigation:
    def test_to_constructor_navigation(self, driver_chrome): # PA Personal Account
        driver_chrome.get(Config.LOGIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''вводим данные'''
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email)
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        login_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_BUTTON))
        login_button.click()
        '''переход на главную страницу'''
        wait.until(EC.url_to_be(Config.MAIN_PAGE_URL))
        personal_account_btn = wait.until(EC.element_to_be_clickable(BurgerLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_btn.click()
        '''переход в профиль'''
        wait.until(EC.url_to_be(Config.PROFILE_PAGE_URL))
        constructor_button = wait.until(EC.element_to_be_clickable(BurgerLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()
        '''переход на главную'''
        wait.until(EC.url_to_be(Config.MAIN_PAGE_URL))
        constructor_title = wait.until(EC.presence_of_element_located(BurgerLocators.CONSTRUCTOR_TITLE_BUTTON))
        assert constructor_title.is_displayed(), 'загоовок "Соберите бургер" is not displayed'

    def test_to_logo_navigation(self, driver_chrome):
        driver_chrome.get(Config.LOGIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        email_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_EMAIL_INPUT))
        email_input.send_keys(DataUser.test_email)
        password_input = wait.until(EC.presence_of_element_located(BurgerLocators.FORM_PASSWORD_INPUT))
        password_input.send_keys(DataUser.test_password)
        login_button = wait.until(EC.element_to_be_clickable(BurgerLocators.FORM_LOGIN_BUTTON))
        login_button.click()
        wait.until(EC.url_to_be(Config.MAIN_PAGE_URL))
        personal_account_btn = wait.until(EC.element_to_be_clickable(BurgerLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_btn.click()
        wait.until(EC.url_to_be(Config.PROFILE_PAGE_URL))
        '''кликаем на логотип'''
        logo_button = wait.until(EC.element_to_be_clickable(BurgerLocators.LOGO_BUTTON))
        logo_button.click()
        wait.until(EC.url_to_be(Config.MAIN_PAGE_URL))
        title_constructor = wait.until(EC.presence_of_element_located(BurgerLocators.CONSTRUCTOR_TITLE_BUTTON))
        assert title_constructor.is_displayed(), 'Название "Соберите бургер" is not displayed'
