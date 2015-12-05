# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import unittest


class WaitForElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_wait_for_photos_button(self):
        self.driver.get("http://travelingtony.weebly.com/")
        button_locator = 'span.wsite-button-inner'
        see_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, button_locator)))
        print see_button

    def test_wait_for_search_field(self):
        self.driver.get("http://travelingtony.weebly.com/")
        search_locator = 'input.wsite-search-input'
        search_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, search_locator)))
        print search_field

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
