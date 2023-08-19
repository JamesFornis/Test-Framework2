import time
import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.cart_page import CartPage
from pages.signup_login_page import SignupPage
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase20(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.cart = CartPage(self.driver)
        self.signup_login = SignupPage(self.driver)

    @pytest.mark.test_case_20
    @file_data("../testdata/logout_data.json")
    def test_case20(self, logout_email, logout_password, card_name, card_num, cvc, exp_month, exp_year, search_keyword):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click on 'Products' button
        go_to_product_page = self.lp.enterHomepage_Products_Page()

        # Verify user is navigated to ALL PRODUCTS page successfully
        go_to_product_page.verify_products_banner()

        # Enter product name in search input and click search button
        go_to_product_page.search_product_input(search_keyword)

        # Verify 'SEARCHED PRODUCTS' is visible
        go_to_product_page.verify_search_products_banner()

        # Verify all the products related to search are visible
        go_to_product_page.verify_search_products_value()

        # Add those products to cart
        go_to_product_page.click_men_tshirt()

        # Click 'Cart' button and verify that products are visible in cart
        go_to_product_page.click_view_cart_btn()
        self.cart.verify_item2()

        # Click 'Signup / Login' button and submit login details
        self.cart.click_signup_login_btn()
        self.signup_login.search_login_input(logout_email,
                                             logout_password)
        # Again, go to Cart page
        self.signup_login.click_cart_btn()

        # Verify that those products are visible in cart after login as well
        self.cart.verify_item_tshirt()
