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
class TestCase1(unittest.TestCase):

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

    # @data(("sad", "asd@mail.com", "12345", "12", "January", "2021", "James", "Fornis", "Cheq Systems Inc", "Cebu City", "Cebu City", "Canada", "Cebu", "Cebu", "6000", "09235873765"), ("jtest", "jtest@mail.com", "12345", "12", "March", "2021", "James", "Fornis", "Cheq Systems Inc", "Cebu City", "Cebu City", "Canada", "Cebu", "Cebu", "6000", "09235873765"))
    # @unpack
    @pytest.mark.test_case_1
    @file_data("../testdata/data.json")
    def test_case1(self, name, email, password, dayinfo, monthinfo, yearinfo, fnames, lnames, compdet, address1, address2, countryname, state, city, zipcode, mobilenum, card_name, card_num, cvc, exp_month, exp_year):
        # launch browser and open url
        # Verify that home page is visible successfully
        # Click on 'Signup / Login' button
        go_to_signup_page = self.lp.enterHomepage_Page()

        # Verify 'New User Signup!' is visible
        go_to_signup_page.verify_signup_banner()

        # Enter name and email address
        # Click 'Signup' button
        go_to_signup_page.search_input(name,
                                       email)

        # Verify that 'ENTER ACCOUNT INFORMATION' is visible
        self.accnt_visibility.verify_account_info_banner()

        # Fill details: Title, Name, Email, Password, Date of birth
        self.accnt_visibility.click_gender()
        self.accnt_visibility.search_accnt_info1(password,
                                                 dayinfo,
                                                 monthinfo,
                                                 yearinfo)

        # Select checkbox Sign up for our newsletter!

        self.chk_newsletter.click_newsletter()

        # Select checkbox 'Receive special offers from our partners!'
        self.chk_partner.click_partner()

        # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        # Click 'Create Account button'

        self.accnt_information.search_accnt_info2(fnames,
                                                  lnames,
                                                  compdet,
                                                  address1,
                                                  address2,
                                                  countryname,
                                                  state,
                                                  city,
                                                  zipcode,
                                                  mobilenum)

        # Verify that 'ACCOUNT CREATED!' is visible
        self.accnt_created.verify_accnt_created_banner()

        # Click 'Continue' button
        self.accnt_created.click_accnt_continue_btn()

        # Verify that 'Logged in as username' is visible
        self.logged_user.verify_logged_username()

        # Click 'Delete Account' button
        self.logged_user.click_delete_btn()

        # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        self.accnt_deleted.verify_accnt_visible()
        self.accnt_deleted.click_continue_btn()
