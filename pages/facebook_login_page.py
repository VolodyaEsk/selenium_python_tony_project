# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException
from facebook_share_page import FacebookSharePage
from UI_map import facebook_login_page_map


class FacebookLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(FacebookLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "id", facebook_login_page_map['username_field_id'])
        except:
            raise IncorrectPageException

    def login(self):
        self.fill_out_field("id", facebook_login_page_map['username_field_id'], self.username)
        self.fill_out_field("id", facebook_login_page_map['password_filed_id'], self.password)
        self.click(10, "name", facebook_login_page_map['login_button_name'])
        return FacebookSharePage(self.driver)


