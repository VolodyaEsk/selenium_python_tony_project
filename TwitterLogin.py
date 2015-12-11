from BaseTestCase import BaseTestCase
from constants import TT_CONSTANTS
from Common import Common


class TwitterLogin(BaseTestCase):

    def setUp(self):
        print 'I am test case'
        super(TwitterLogin, self).setUp()
        productPageURL = TT_CONSTANTS['Base_URL']+"store/p4/Lope_Lunch_By_The_Pool.html"
        self.navigate_to_page(productPageURL)
        common_obj = Common(self.driver)
        common_obj.wait_for_element_visibility(10,
                                               "id",
                                               "wsite-com-product-option-Quantity"
                                               )
        mainWindowHandle  = self.driver.window_handles
        common_obj.click(10, "xpath", "//a[@class='wsite-com-product-social-twitter']")
        allWindowsHandles = self.driver.window_handles
        for handle in allWindowsHandles:
            if handle != mainWindowHandle[0]:
                common_obj.switch_to_window(handle)
                break
        common_obj.wait_for_element_visibility(10,
                                               "id",
                                               "username_or_email"
                                               )
        common_obj.fill_out_field("id",
                                  "username_or_email",
                                  TT_CONSTANTS['Twitter_Username']
                                  )
        common_obj.fill_out_field("id",
                                  "password",
                                  TT_CONSTANTS['Twitter_Password']
                                  )
        common_obj.click(10, "xpath", "//input[@class='button selected submit']")
        common_obj.wait_for_element_visibility(10,
                                               "xpath",
                                               "//input[@id='char-count']/following-sibling::input"
                                               )

    def tearDown(self):
        super(TwitterLogin, self).tearDown()