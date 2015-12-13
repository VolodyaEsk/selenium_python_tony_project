# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException
from twitter_share_page import TwitterSharePage
from UI_map import twitter_login_page_mao

class TwitterLoginPage(BasePage):

    def __init__(self, driver, username, password):
        super(TwitterLoginPage, self).__init__(driver)
        self.username = username
        self.password = password

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "id", twitter_login_page_mao['username_field_id'])
        except:
            raise IncorrectPageException

    def login(self):
        self.fill_out_field("id", twitter_login_page_mao['username_field_id'], self.username)
        self.fill_out_field("id", twitter_login_page_mao['password_field_id'], self.password)
        self.click(10, "xpath", twitter_login_page_mao['login_button_xpath'])
        return TwitterSharePage(self.driver)


