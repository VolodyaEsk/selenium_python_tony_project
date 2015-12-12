# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException
from twitter_share_page import TwitterSharePage


class TwitterLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(TwitterLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "id", "username_or_email")
        except:
            raise IncorrectPageException

    def login(self):
        self.fill_out_field("id", "username_or_email", self.username)
        self.fill_out_field("id", "password", self.password)
        self.click(10, "xpath", "//input[@class='button selected submit']")
        return TwitterSharePage(self.driver)


