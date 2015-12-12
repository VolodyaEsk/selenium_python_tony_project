# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException


class FacebookSharePage(BasePage):

    def __init__(self, driver):
        super(FacebookSharePage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "name", "share")
        except:
            raise IncorrectPageException

    def share(self):
        self.click(10, "name", "share")
