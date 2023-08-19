import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.accnt_info_page import AccntInfo
from pages.accnt_created_page import AccntCreated
from pages.logged_page import LoggedPage
from pages.accnt_deleted_page import AccntDeleted
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase5(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.accnt_visibility = AccntInfo(self.driver)
        self.chk_newsletter = AccntInfo(self.driver)
        self.chk_partner = AccntInfo(self.driver)
        self.accnt_information = AccntInfo(self.driver)
        self.accnt_created = AccntCreated(self.driver)
        self.logged_user = LoggedPage(self.driver)
        self.accnt_deleted = AccntDeleted(self.driver)

    @pytest.mark.test_case_5
    @file_data("../testdata/registered_signup_data.json")
    def test_case5(self, reg_name, reg_email):
        # launch browser and open url
        # Verify that home page is visible successfully
        # Click on 'Signup / Login' button
        go_to_signup_page = self.lp.enterHomepage_Page()

        # Verify 'New User Signup!' is visible
        go_to_signup_page.verify_signup_banner()

        # Enter name and already registered email address
        # Click 'Signup' button
        go_to_signup_page.search_input(reg_name,
                                       reg_email)

        # Verify error 'Email Address already exist!' is visible
        go_to_signup_page.verify_registered_signup_banner()
