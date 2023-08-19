import time
import pytest
import unittest
from pages.launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestCase12(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    @pytest.mark.test_case_12
    def test_case12(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click 'Products' button
        go_to_product_page = self.lp.enterHomepage_Products_Page()

        # Hover over first product and click 'Add to cart'
        go_to_product_page.scroll_and_click_add_to_cart_btn()

        # Click 'Continue Shopping' button
        go_to_product_page.click_continue_shopping_btn()

        # Hover over second product and click 'Add to cart'
        go_to_product_page.click_add_to_cart2_btn()

        # Click 'View Cart' button
        go_to_cart_page = self.lp.enterHomepage_Cart_Page()

        # Verify both products are added to Cart
        go_to_cart_page.verify_item1()
        go_to_cart_page.verify_item2()

        # Verify their prices, quantity and total price
        go_to_cart_page.verify_cart()
