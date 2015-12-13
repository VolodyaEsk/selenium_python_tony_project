from constants import TT_CONSTANTS
from Base import Base
from Common import Common
from selenium.webdriver.common.keys import Keys
import unittest
import time
from nose.plugins.attrib import attr


class SearchVerifyPicture(Base, unittest.TestCase):

    def setUp(self):
        super(SearchVerifyPicture, self).setUp()
        self.navigate_to_page(TT_CONSTANTS['Base_URL'])

    @attr(group="other")
    def test_search_verify_picture(self):
        common_obj = Common(self.driver)
        elem = common_obj.wait_for_element_visibility(5, "name", 'q')
        common_obj.fill_out_field('name', 'q', 'leatherback')
        elem.send_keys(Keys.RETURN)
        common_obj.wait_for_element_visibility(5, 'xpath',
                                               "//div[@class='wsite-search-product-image-container']"
                                               )
        time.sleep(3)

    def tearDown(self):
        super(SearchVerifyPicture, self).tearDown()


if __name__ == "__main__":
    unittest.main()