import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_chrome
from src.locators import BurgerLocators
from src.config import Config



class TestSections:
    def test_section_breads(self, driver_chrome):
        driver_chrome.get(Config.MAIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''кликаем по секции соусы'''
        sauces_no_select = wait.until(EC.element_to_be_clickable(BurgerLocators.SAUCES_NO_SELECT))
        sauces_no_select.click()
        '''кликаем по секции булки'''
        bread_no_select = wait.until(EC.element_to_be_clickable(BurgerLocators.BREADS_NO_SELECT))
        bread_no_select.click()
        bread_select = wait.until(EC.presence_of_element_located(BurgerLocators.BREADS_SELECT))
        assert 'tab_tab_type_current__2BEPc' in bread_select.get_attribute('class')

    def test_section_sauces(self, driver_chrome):
        driver_chrome.get(Config.MAIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''кликаем по секции соусы'''
        sauces_no_select = wait.until(EC.element_to_be_clickable(BurgerLocators.SAUCES_NO_SELECT))
        sauces_no_select.click()
        sauces_select = wait.until(EC.presence_of_element_located(BurgerLocators.SAUCES_SELECT))
        assert 'tab_tab_type_current__2BEPc' in sauces_select.get_attribute('class')


    def test_section_toppings(self, driver_chrome):
        driver_chrome.get(Config.MAIN_PAGE_URL)
        wait = WebDriverWait(driver_chrome, 30)
        '''кликаем по секции начинки'''
        topping_no_select = wait.until(EC.element_to_be_clickable(BurgerLocators.TOPPING_NO_SELECT))
        topping_no_select.click()
        topping_select = wait.until(EC.presence_of_element_located(BurgerLocators.TOPPING_SELECT))
        assert 'tab_tab_type_current__2BEPc' in topping_select.get_attribute('class')

