# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import unittest


class Assertsions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(15)

    def test_assert_title(self):
        self.driver.get("http://travelingtony.weebly.com/")
        self.assertEqual(self.driver.title, "Traveling Tony's Photography - Welcome")

    def test_contact_form_empty_last_name(self):
        self.driver.get("http://travelingtony.weebly.com/")

        contact_locator = "//a[.='Contact']"
        name_field_locator = "//input[contains(@name, 'first')]"
        # last_name_field_locator = "//input[contains(@name, 'last')]"
        email_field_locator = "//div/label[contains(text(), 'Email')]/following-sibling::div/input"
        text_area_locator = "textarea"
        submit_button_locator = 'span.wsite-button-inner'
        error_text_locator = '//form/following-sibling::div'

        self.wait.until(EC.element_to_be_clickable((By.XPATH, contact_locator))).click()
        name_field_element = self.wait.until(EC.presence_of_element_located((By.XPATH, name_field_locator)))
        name_field_element.send_keys("Romeo")
        email_field_element = self.wait.until(EC.presence_of_element_located((By.XPATH, email_field_locator)))
        email_field_element.send_keys("romeolucky@gmail.co")
        text_area_element = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, text_area_locator)))
        text_area_element.send_keys("some complaints!!")
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, submit_button_locator))).click()

        error_text = self.driver.find_element_by_xpath(error_text_locator).text
        self.assertEqual('Please correct the highlighted fields', error_text, "ERROR TEXT IS NOT EQUAL")

    def test_select_drop_down_option(self):
        self.driver.get("http://travelingtony.weebly.com/store/p4/Lope_Lunch_By_The_Pool.html")
        drop_down_id = "wsite-com-product-option-Quantity"
        drop_down_element = self.wait.until(lambda driver: driver.find_element_by_id(drop_down_id))
        select = Select(drop_down_element)
        select.select_by_visible_text('2')
        select.select_by_index(0)
        select.select_by_value('1')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
