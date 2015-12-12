# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException


class ContactPage(BasePage):

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "xpath", "//input[contains(@name, 'first')]")
        except:
            raise IncorrectPageException

    def submit_request(self):
        self.fill_out_field("xpath", "//input[contains(@name, 'first')]", "Paul")
        self.fill_out_field("xpath", "//input[contains(@name, 'last')]", "Pierce")
        self.fill_out_field("xpath", "//div/label[contains(text(), 'Email')]/following-sibling::div/input",
                            "contactemail@test.com")
        self.fill_out_field("xpath", "//textarea", "My comment")
        self.click(10, "xpath", "//span[.='Submit']")
        self.wait_for_element_visibility(10, "xpath", "//div[contains(text(), 'Thank you')]")

    def validation_check(self):
        self.fill_out_field("xpath", "//input[contains(@name, 'first')]", "Paul")
        self.fill_out_field("xpath", "//input[contains(@name, 'last')]", "Pierce")
        self.fill_out_field("xpath", "//div/label[contains(text(), 'Email')]/following-sibling::div/input",
                            "contactemail@")
        self.fill_out_field("xpath", "//textarea", "My comment")
        self.click(10, "xpath", "//span[.='Submit']")
        return self
