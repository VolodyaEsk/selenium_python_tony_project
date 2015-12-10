# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
# import time


class ClickSubmenu(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.maximize_window()
        self.url = "http://travelingtony.weebly.com/"

    def test_click_sub_menu(self):
        driver.get(self.url)
        # Locators
        africa_menu_locator = "//a[.='Africa']"
        gabon_sub_menu_locator = "//a[contains(@href, 'gabon')]"
        impala_div_locator = "//div[@class='wsite-header']"

        africa_menu_element = WebDriverWait(driver, 5).\
            until(lambda driver: driver.find_element_by_xpath(africa_menu_locator))

        actions = ActionChains(driver)
        actions.move_to_element(africa_menu_element)
        # actions.click(driver.find_element_by_xpath(gabon_sub_menu_locator) # this way is not working
        actions.perform()
        gabon_sub_menu_element = WebDriverWait(driver, 5).\
            until(EC.visibility_of_element_located((By.XPATH, gabon_sub_menu_locator)))
        gabon_sub_menu_element.click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(impala_div_locator))

    def test_send_keys(self):
        driver.get(self.url)
        # Locators
        search_field_name = 'q'
        turtle_picture_locator = "//span[@title='Leatherback Turtle Picture']"

        search_field_element = WebDriverWait(driver, 5).\
            until(lambda driver: driver.find_element_by_name(search_field_name))

        actions = ActionChains(driver)
        actions.send_keys_to_element(search_field_element, "Leatherback")
        actions.send_keys_to_element(search_field_element, Keys.RETURN)
        actions.perform()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(turtle_picture_locator))

    def test_actions_quantity(self):
        url = 'http://travelingtony.weebly.com/store/p4/Lope_Lunch_By_The_Pool.html'
        driver.get(url)
        # Locators
        quantity_id = 'wsite-com-product-option-Quantity'

        quantity_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(quantity_id))

        actions = ActionChains(driver)
        actions.send_keys_to_element(quantity_element, Keys.ENTER)
        actions.send_keys_to_element(quantity_element, Keys.ARROW_DOWN)
        actions.send_keys_to_element(quantity_element, Keys.ARROW_DOWN)
        actions.perform()
        # Just using time.sleep() so that you can see the last webdriver action.
        # It is not recommended using it in your tests
        # time.sleep(5)

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
