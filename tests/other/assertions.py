# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import unittest


class Assertsions(unittest.TestCase):

    base_url = "http://travelingtony.weebly.com/"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(15)

    def test_assert_title(self):
        self.driver.get(self.base_url)
        self.assertEqual(self.driver.title, "Traveling Tony's Photography - Welcome")

    def test_contact_form_empty_last_name(self):
        self.driver.get(self.base_url)

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
        self.driver.get(self.base_url + "store/p4/Lope_Lunch_By_The_Pool.html")
        drop_down_id = "wsite-com-product-option-Quantity"
        drop_down_element = self.wait.until(lambda driver: driver.find_element_by_id(drop_down_id))
        select = Select(drop_down_element)
        select.select_by_visible_text('2')
        select.select_by_index(0)
        select.select_by_value('1')

    def test_add_picture_to_cart(self):
        self.driver.get(self.base_url)

        search_locator = 'wsite-search-input'
        product_locator = "//span[@title='Leatherback Turtle Picture']"
        quantity_locator = 'wsite-com-product-option-Quantity'
        add_to_cart_button_locator = "wsite-com-product-add-to-cart"
        pop_up_div_locator = 'wsite-com-issue-overlay'
        pop_up_p_locator = "//div[@id='wsite-com-issue-overlay']/p"

        search_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, search_locator)))
        search_element.send_keys("leatherback")
        search_element.send_keys(Keys.RETURN)

        product_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, product_locator)))
        product_element.click()
        select = Select(self.driver.find_element_by_id(quantity_locator))
        select.select_by_visible_text('3')

        add_to_cart_button_element = self.wait.until(EC.element_to_be_clickable((By.ID, add_to_cart_button_locator)))
        print add_to_cart_button_element
        add_to_cart_button_element.click()

        pop_up_div_element = self.wait.until(EC.presence_of_element_located((By.ID, pop_up_div_locator)))
        self.assertTrue(bool(pop_up_div_element))

        pop_up_p_element = self.driver.find_element_by_xpath(pop_up_p_locator)
        actual_text = pop_up_p_element.text
        print actual_text
        self.assertEqual(actual_text, "This store is not yet accepting payments.\nPlease check back later.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
