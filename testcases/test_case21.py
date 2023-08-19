import time
import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.cart_page import CartPage
from pages.signup_login_page import SignupPage
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase21(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.cart = CartPage(self.driver)
        self.signup_login = SignupPage(self.driver)

    @pytest.mark.test_case_21
    @file_data("../testdata/review_data.json")
    def test_case21(self, rev_name, rev_email, rev_input):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Click on 'Products' button
        go_to_product_page = self.lp.enterHomepage_Products_Page()

        # Verify user is navigated to ALL PRODUCTS page successfully
        go_to_product_page.verify_products_banner()

        # Click on 'View Product' button
        go_to_product_page.click_view_product_btn()

        # Verify 'Write Your Review' is visible
        go_to_product_page.verify_write_your_review_banner()

        # Enter name, email and review
        # Click 'Submit' button
        go_to_product_page.search_review(rev_name,
                                         rev_email,
                                         rev_input)

        # Verify success message 'Thank you for your review.'
        go_to_product_page.verify_thanks_for_review_banner()
