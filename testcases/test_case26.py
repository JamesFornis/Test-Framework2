import time
import pytest
import unittest
from pages.launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestCase26(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    @pytest.mark.test_case_26
    def test_case26(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        self.lp.enterLaunch_Page()

        # Scroll down page to bottom
        self.lp.scroll_down()

        # Verify 'SUBSCRIPTION' is visible
        self.lp.verify_subscription_banner()

        # Scroll up page to top
        self.lp.scroll_up()

        # Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
        self.lp.verify_full_fledged_banner()
