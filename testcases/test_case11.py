import time
import pytest
import unittest
from pages.launch_page import LaunchPage
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase11(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    @pytest.mark.test_case_11
    @file_data("../testdata/email_data.json")
    def test_case11(self, email):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click 'Cart' button
        go_to_cart_page = self.lp.enterHomepage_Cart_Page()

        # Scroll down to footer
        go_to_cart_page.scroll_down_cart()

        # Verify text 'SUBSCRIPTION'
        go_to_cart_page.verify_cart_subscription_banner()

        # Enter email address in input and click arrow button
        go_to_cart_page.search_cart_subscribe(email)

        # Verify success message 'You have been successfully subscribed!' is visible
        go_to_cart_page.verify_cart_success_message()
