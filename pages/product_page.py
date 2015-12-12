# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException
from facebook_login_page import FacebookLoginPage
from twitter_login_page import TwitterLoginPage
from constants import TT_CONSTANTS


class ProductPage(BasePage):

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "id", "wsite-com-product-option-Quantity")
        except:
            raise IncorrectPageException

    def click_on_facebook_share_button(self):
        main_window_handle = self.driver.window_handles
        self.click(10, "xpath", "//a[@title='Share on Facebook']")
        all_windows_handles = self.driver.window_handles
        for handle in all_windows_handles:
            if handle != main_window_handle[0]:
                self.switch_to_window(handle)
                break
        return FacebookLoginPage(self.driver,
                                 TT_CONSTANTS['Facebook_Username'],
                                 TT_CONSTANTS['Facebook_Password']
                                 )

    def click_on_twitter_share_button(self):
        main_window_handle = self.driver.window_handles
        self.click(10, "xpath", "//a[@class='wsite-com-product-social-twitter']")
        all_windows_handles = self.driver.window_handles
        for handle in all_windows_handles:
            if handle != main_window_handle[0]:
                self.switch_to_window(handle)
                break
        return TwitterLoginPage(self.driver,
                                TT_CONSTANTS['Twitter_Username'],
                                TT_CONSTANTS['Twitter_Password']
                                )