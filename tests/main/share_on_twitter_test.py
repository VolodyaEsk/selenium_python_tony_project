from TwitterLogin import TwitterLogin
from pages.twitter_share_page import TwitterSharePage
import unittest
import time
import nose
from nose.plugins.attrib import attr


class ShareOnTwitterTest(TwitterLogin, unittest.TestCase):

    def setUp(self):
        super(ShareOnTwitterTest, self).setUp()

    @attr(priority="high")
    @attr(group="socialNetworking")
    def test_tweet_on_twitter_test(self):
        share_on_facebook_page_obj = TwitterSharePage(self.driver)
        share_on_facebook_page_obj.share()
        """
        Just using time.sleep() so that you see the last webdriver action.
        It is not recommended using this in your tests.
        """
        time.sleep(2)

    def tearDown(self):
        super(ShareOnTwitterTest, self).tearDown()


if __name__ == "__main__":
    nose.main()


