# -*- coding: utf-8 -*-

from base_page import BasePage
from base_page import IncorrectPageException
from UI_map import contact_page_map


class ContactPage(BasePage):

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(5, "xpath", "//input[contains(@name, 'first')]")
        except:
            raise IncorrectPageException

    def submit_request(self):
        self.fill_out_field("xpath", contact_page_map['first_name_field_xpath'], "Paul")
        self.fill_out_field("xpath", contact_page_map['last_name_field_xpath'], "Pierce")
        self.fill_out_field("xpath", contact_page_map['email_field_xpath'], "contactemail@test.com")
        self.fill_out_field("xpath", contact_page_map['comment_field_xpath'], "My comment")
        self.click(10, "xpath", contact_page_map['submit_button_xpath'])
        self.wait_for_element_visibility(10, "xpath", contact_page_map['thank_you_message_xpath'])

    def validation_check(self):
        self.fill_out_field("xpath", contact_page_map['first_name_field_xpath'], "Paul")
        self.fill_out_field("xpath", contact_page_map['last_name_field_xpath'], "Pierce")
        self.fill_out_field("xpath", contact_page_map['email_field_xpath'], "contactemail@")
        self.fill_out_field("xpath", contact_page_map['comment_field_xpath'], "My comment")
        self.click(10, "xpath", contact_page_map['submit_button_xpath'])
        return self
