import time
import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("setup")
class TestCase22(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.cart = CartPage(self.driver)

    @pytest.mark.test_case_22
    def test_case22(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Scroll to bottom of page
        self.lp.enterLaunch_Page()
        self.lp.scroll_down()

        # Verify 'RECOMMENDED ITEMS' are visible
        self.lp.verify_recommended_items_banner()

        # Click on 'Add To Cart' on Recommended product
        self.lp.click_add_to_cart_btn()

        # Click on 'View Cart' button
        self.lp.click_view_cart_btn()

        # Verify that product is displayed in cart page
        self.cart.verify_cart_item()
