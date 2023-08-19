import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("setup")
class TestCase13(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.product = ProductsPage(self.driver)
        self.cart = CartPage(self.driver)

    @pytest.mark.test_case_13
    def test_case13(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Click 'View Product' for any product on home page
        self.lp.scroll_and_click_view_product_btn()

        # Verify product detail is opened
        self.product.verify_view_product_name_label()

        # Increase quantity to 4
        # Click 'Add to cart' button
        # Click 'View Cart' button
        self.product.input_product_qty()
        self.product.search_view_product_add_to_cart()

        # Verify that product is displayed in cart page with exact quantity
        self.cart.verify_view_product_qty()
