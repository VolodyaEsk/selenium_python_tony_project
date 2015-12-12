# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException


class TwitterSharePage(BasePage):

    def __init__(self, driver):
        super(TwitterSharePage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5,  "xpath", "//input[@id='char-count']/following-sibling::input")
        except:
            raise IncorrectPageException

    def share(self):
        self.click(10,  "xpath", "//input[@id='char-count']/following-sibling::input")
