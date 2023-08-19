import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.logged_page import LoggedPage
from pages.accnt_deleted_page import AccntDeleted
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase2(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.logged_user = LoggedPage(self.driver)
        self.accnt_deleted = AccntDeleted(self.driver)

    @pytest.mark.test_case_2
    @file_data("../testdata/login_data.json")
    def test_case2(self, log_email, log_password):
        # Launch browser
        # Navigate to url'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click on 'Signup / Login' button
        go_to_signup_page = self.lp.enterHomepage_Page()

        # Verify 'Login to your account' is visible
        go_to_signup_page.verify_login_banner()

        # Enter correct email address and password
        # Click 'login' button
        go_to_signup_page.search_login_input(log_email,
                                             log_password)

        # Verify that 'Logged in as username' is visible
        self.logged_user.verify_logged_username()

        # Click 'Delete Account' button
        self.logged_user.click_delete_btn()
        # Verify that 'ACCOUNT DELETED!' is visible
        self.accnt_deleted.verify_accnt_visible()
        self.accnt_deleted.click_continue_btn()
