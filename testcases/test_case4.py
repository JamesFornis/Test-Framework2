import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.logged_page import LoggedPage
from pages.accnt_deleted_page import AccntDeleted
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase4(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.logged_user = LoggedPage(self.driver)
        self.accnt_deleted = AccntDeleted(self.driver)

    @pytest.mark.test_case_4
    @file_data("../testdata/logout_data.json")
    def test_case4(self, logout_email, logout_password, card_name, card_num, cvc, exp_month, exp_year):
        # Launch browser
        # Navigate to url'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click on 'Signup / Login' button
        go_to_signup_page = self.lp.enterHomepage_Page()

        # Verify 'Login to your account' is visible
        go_to_signup_page.verify_login_banner()

        # Enter correct email address and password
        # Click 'login' button
        go_to_signup_page.search_login_input(logout_email,
                                             logout_password)

        # Verify that 'Logged in as username' is visible
        self.logged_user.verify_logged_username()

        # Click 'Logout' button
        self.logged_user.click_logout_btn()

        # Verify that user is navigated to login page
        go_to_signup_page.verify_login_banner()
