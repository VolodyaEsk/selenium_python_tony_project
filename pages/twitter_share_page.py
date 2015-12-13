# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException
from UI_map import twitter_share_page_map


class TwitterSharePage(BasePage):

    def __init__(self, driver):
        super(TwitterSharePage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5,  "xpath", twitter_share_page_map['tweet_link_button_xpath'])
        except:
            raise IncorrectPageException

    def share(self):
        self.click(10,  "xpath", twitter_share_page_map['tweet_link_button_xpath'])
