import pytest
import unittest
from pages.launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestCase7(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    @pytest.mark.test_case_7
    def test_case7(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click on 'Test Cases' button
        go_to_test_cases_page = self.lp.enterHomepage_TestCases_Page()

        # Verify user is navigated to test cases page successfully
        go_to_test_cases_page.verify_test_cases_banner()
