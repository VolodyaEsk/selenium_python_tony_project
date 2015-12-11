from TwitterLogin import TwitterLogin
from Common import Common
import unittest
import time


class ShareOnFacebookTest(TwitterLogin, unittest.TestCase):

    def setUp(self):
        super(ShareOnFacebookTest, self).setUp()

    def test_SendRequestTest(self):
        common_obj = Common(self.driver)
        common_obj.click(10, "xpath", "//input[@id='char-count']/following-sibling::input")
        """
        Just using time.sleep() so that you see the last webdriver action.
        It is not recommended using this in your tests.
        """
        time.sleep(5)

    def tearDown(self):
        super(ShareOnFacebookTest, self).tearDown()


if __name__ == "__main__":
    unittest.main()


