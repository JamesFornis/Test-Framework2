import time
import pytest
import unittest
from pages.launch_page import LaunchPage
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase10(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    @pytest.mark.test_case_10
    @file_data("../testdata/email_data.json")
    def test_case10(self, email):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        self.lp.enterLaunch_Page()

        # Scroll down to footer
        self.lp.scroll_down()

        # Verify text 'SUBSCRIPTION'
        self.lp.verify_subscription_banner()

        # Enter email address in input and click arrow button
        self.lp.search_subscribe(email)

        # Verify success message 'You have been successfully subscribed!' is visible
        self.lp.verify_success_message()
