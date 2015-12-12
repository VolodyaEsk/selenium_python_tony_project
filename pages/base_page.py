# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import LocatorMode
from abc import abstractmethod


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    @abstractmethod
    def _verify_page(self):
        """
        This method verifies that we are on the correct page.
        """

    def wait_for_element_visibility(self, wait_time, locator_mode, locator):
        element = None
        if locator_mode == LocatorMode.ID:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.visibility_of_element_located((By.ID, locator)))
        elif locator_mode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.visibility_of_element_located((By.NAME, locator)))
        elif locator_mode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.visibility_of_element_located((By.XPATH, locator)))
        elif locator_mode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def wait_until_element_clickable(self, wait_time, locator_mode, locator):
        element = None
        if locator_mode == LocatorMode.ID:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.element_to_be_clickable((By.ID, locator)))
        elif locator_mode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.element_to_be_clickable((By.NAME, locator)))
        elif locator_mode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.element_to_be_clickable((By.XPATH, locator)))
        elif locator_mode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, wait_time).\
                until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def find_element(self, locator_mode, locator):
        element = None
        if locator_mode == LocatorMode.ID:
            element = self.driver.find_element_by_id(locator)
        elif locator_mode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(locator)
        elif locator_mode == LocatorMode.XPATH:
            element = self.driver.find_element_by_xpath(locator)
        elif locator_mode == LocatorMode.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def fill_out_field(self, locator_mode, locator, text):
        self.find_element(locator_mode, locator).clear()
        self.find_element(locator_mode, locator).send_keys(text)

    def click(self, wait_time, locator_mode, locator):
        self.wait_until_element_clickable(wait_time, locator_mode, locator).click()


class IncorrectPageException(Exception):
    """
    This exception should be thrown when trying to instantiate the wrong page.
    """
