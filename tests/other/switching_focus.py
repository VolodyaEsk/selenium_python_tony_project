# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import unittest
import time


class SwitchToWindow(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.maximize_window()

    def test_switch_to_Facebook_window(self):
        url = 'http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html'
        driver.get(url)
        # Locators
        FB_sharing_link_locator = 'a.wsite-com-product-social-facebook'
        FB_username_id = 'email'
        FB_password_field_id = 'pass'
        FB_login_button_name = 'login'
        FB_share_link_button_name = 'share'

        # FB credentials
        FB_username = 'eskidev@gmail.com'
        FB_password = 'tester12345'

        FB_sharing_link_element = WebDriverWait(driver, 10).\
            until(lambda driver: driver.find_element_by_css_selector(FB_sharing_link_locator))

        # Get the main Window handle
        main_window_handle1 = driver.current_window_handle
        main_window_handle2 = driver.window_handles
        print type(main_window_handle1)
        print type(main_window_handle2)
        print main_window_handle1, main_window_handle2
        print main_window_handle1[0] == main_window_handle2

        # Click the sharing FB element
        FB_sharing_link_element.click()

        # Get all window handles
        all_window_handles = driver.window_handles
        for handle in all_window_handles:
            if handle not in main_window_handle2:
                driver.switch_to_window(handle)
                break

        FB_username_elem = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(FB_username_id))
        FB_password_elem = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(FB_password_field_id))
        FB_login_button_elem = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_name(FB_login_button_name))

        FB_username_elem.send_keys(FB_username)
        FB_password_elem.send_keys(FB_password)
        FB_login_button_elem.click()
        WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_name(FB_share_link_button_name))

    def test_switch_and_share_window_twitter(self):
        url = 'http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html'
        driver.get(url)

        # Locators
        twitter_sharing_link_locator_css = 'a.wsite-com-product-social-twitter'
        twitter_username_id = 'username_or_email'
        twitter_password_id = 'password'
        twitter_submit_button_class = 'input.button.selected.submit'
        twitter_share_button_class = 'input.button.selected.submit'

        # Twitter credential
        twitter_username = 'eskidev@gmail.com'
        twitter_password = 'tester12345'

        # Get current handle
        main_current_window = driver.current_window_handle

        wait = WebDriverWait(driver, 5)
        twitter_sharing_elem = wait.until(lambda driver: driver.
                                          find_element_by_css_selector(twitter_sharing_link_locator_css))
        twitter_sharing_elem.click()
        # Get all window handles
        all_window_handles = driver.window_handles
        for handle in all_window_handles:
            if handle != main_current_window:
                driver.switch_to_window(handle)
                break
        tt_username_elem = wait.until(lambda driver: driver.find_element_by_id(twitter_username_id))
        tt_username_elem.send_keys(twitter_username)

        tt_password_elem = wait.until(lambda driver: driver.find_element_by_id(twitter_password_id))
        tt_password_elem.send_keys(twitter_password)

        wait.until(lambda driver: driver.find_element_by_css_selector(twitter_submit_button_class)).click()
        wait.until(lambda driver: driver.find_element_by_css_selector(twitter_share_button_class)).click()

        # time.sleep(4)



    def test_focus_to_alert(self):
        url = 'http://www.tizag.com/javascriptT/javascriptconfirm.php'
        driver.get(url)

        # Locators
        button_locator = '//input[@value="Leave Tizag.com"]'
        button_element = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath(button_locator))
        button_element.click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to_alert()
        alert.dismiss()
        # time.sleep(4) just for visual assurance of success

    def test_switch_to_frame(self):
        url = 'http://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm'
        driver.get(url)

        # Locators
        iframe_id = 'iframeResult'
        try_it_button_locator = '//button[.="Try it"]'

        iframe_elem = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id(iframe_id))
        driver.switch_to_frame(iframe_elem)

        try_it_button_elem = WebDriverWait(driver, 5).\
            until(lambda driver: driver.find_element_by_xpath(try_it_button_locator))
        try_it_button_elem.click()

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()
