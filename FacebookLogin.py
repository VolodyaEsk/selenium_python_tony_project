from Base import Base
from constants import TT_CONSTANTS
from pages.product_page import ProductPage
from pages.facebook_login_page import FacebookLoginPage


class FacebookLogin(Base):

    def setUp(self):
        super(FacebookLogin, self).setUp()
        product_page_url = TT_CONSTANTS['Base_URL']+"store/p1/Leatherback_Turtle_Picture.html"
        self.navigate_to_page(product_page_url)
        product_page_obj = ProductPage(self.driver)
        product_page_obj.click_on_facebook_share_button()
        action = FacebookLoginPage(self.driver,
                                   TT_CONSTANTS['Facebook_Username'],
                                   TT_CONSTANTS['Facebook_Password']
                                   )
        action.login()

    def tearDown(self):
        super(FacebookLogin, self).tearDown()
