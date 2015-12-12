from FacebookLogin import FacebookLogin
from pages.facebook_share_page import FacebookSharePage
import unittest
import time


class ShareOnFacebookTest(FacebookLogin, unittest.TestCase):

    def setUp(self):
        super(ShareOnFacebookTest, self).setUp()

    def test_share_on_facebook_test(self):
        share_on_facebook_page_obj = FacebookSharePage(self.driver)
        share_on_facebook_page_obj.share()
        """
        Just using time.sleep() so that you see the last webdriver action.
        It is not recommended using this in your tests.
        """
        time.sleep(2)

    def tearDown(self):
        super(ShareOnFacebookTest, self).tearDown()


if __name__ == "__main__":
    unittest.main()


