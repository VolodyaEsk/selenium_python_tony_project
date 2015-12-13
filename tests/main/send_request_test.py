from constants import TT_CONSTANTS
from Base import Base
from pages.contact_page import ContactPage
import unittest
import time
import nose
from nose.plugins.attrib import attr


class SendRequestTest(Base, unittest.TestCase):

    def setUp(self):
        super(SendRequestTest, self).setUp()
        self.navigate_to_page(TT_CONSTANTS['Base_URL'] + "contact")

    @attr(priority="high")
    @attr(group="other")
    def test_send_request_test(self):
        contact_page = ContactPage(self.driver)
        contact_page.submit_request()
        """
        Just using time.sleep() so that you see the last webdriver action.
        It is not recommended using this in your tests.
        """
        time.sleep(2)

    @attr(priority="high")
    @attr(group="other")
    def test_validation(self):
        contact_page = ContactPage(self.driver)
        contact_page.validation_check()
        """
        Just using time.sleep() so that you see the last webdriver action.
        It is not recommended using this in your tests.
        """
        time.sleep(2)

    def tearDown(self):
        super(SendRequestTest, self).tearDown()


if __name__ == "__main__":
    nose.main()


