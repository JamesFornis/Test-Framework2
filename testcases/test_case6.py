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
class TestCase6(unittest.TestCase):

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

    @pytest.mark.test_case_6
    @file_data("../testdata/contact_data.json")
    def test_case6(self, contact_name, contact_email, contact_subject, contact_message):
        # launch browser and open url
        # Verify that home page is visible successfully
        # Click on 'Contact Us' button
        go_to_contact_us_page = self.lp.enterHomepage_ContactUs_Page()

        # Verify 'GET IN TOUCH' is visible
        go_to_contact_us_page.verify_get_in_touch_banner()

        # Enter name, email, subject and message
        go_to_contact_us_page.search_contact_input(contact_name,
                                                   contact_email,
                                                   contact_subject,
                                                   contact_message)
        # Upload file
        go_to_contact_us_page.click_upload_file_btn()

        # Click 'Submit' button
        # Click OK button
        go_to_contact_us_page.click_submit_btn()

        # Verify success message 'Success! Your details have been submitted successfully.' is visible
        go_to_contact_us_page.verify_success_banner()

        # Click 'Home' button and verify that landed to home page successfully
        go_to_contact_us_page.get_home_btn()
