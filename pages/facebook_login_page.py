# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException
from facebook_share_page import FacebookSharePage


class FacebookLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(FacebookLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "id", "email")
        except:
            raise IncorrectPageException

    def login(self):
        self.fill_out_field("id", "email", self.username)
        self.fill_out_field("id", "pass", self.password)
        self.click(10, "name", "login")
        return FacebookSharePage(self.driver)


