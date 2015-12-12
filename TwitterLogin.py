from Base import Base
from constants import TT_CONSTANTS
from pages.product_page import ProductPage


class TwitterLogin(Base):

    def setUp(self):
        super(TwitterLogin, self).setUp()
        product_page_url = TT_CONSTANTS['Base_URL']+"store/p2/Ogooue_River.html"
        self.navigate_to_page(product_page_url)
        product_page_obj = ProductPage(self.driver)
        action = product_page_obj.click_on_twitter_share_button()
        action.login()

    def tearDown(self):
        super(TwitterLogin, self).tearDown()