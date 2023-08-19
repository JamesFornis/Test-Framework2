import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.accnt_info_page import AccntInfo
from pages.accnt_created_page import AccntCreated
from pages.logged_page import LoggedPage
from pages.accnt_deleted_page import AccntDeleted
from pages.cart_page import CartPage
from ddt import ddt, file_data
from pages.payment_page import PaymentPage


@pytest.mark.usefixtures("setup")
@ddt
class TestCase23(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.payment = PaymentPage(self.driver)
        self.cart = CartPage(self.driver)
        self.accnt_visibility = AccntInfo(self.driver)
        self.chk_newsletter = AccntInfo(self.driver)
        self.chk_partner = AccntInfo(self.driver)
        self.accnt_information = AccntInfo(self.driver)
        self.accnt_created = AccntCreated(self.driver)
        self.logged_user = LoggedPage(self.driver)
        self.accnt_deleted = AccntDeleted(self.driver)

    @pytest.mark.test_case_23
    @file_data("../testdata/data.json")
    def test_case23(self, name, email, password, dayinfo, monthinfo, yearinfo, fnames, lnames, compdet, address1, address2, countryname, state, city, zipcode, mobilenum, card_name, card_num, cvc, exp_month, exp_year):
        # launch browser and open url
        # Verify that home page is visible successfully
        # Click on 'Signup / Login' button
        go_to_signup_page = self.lp.enterHomepage_Page()

        # Fill all details in Signup and create account
        go_to_signup_page.search_input(name,
                                       email)
        self.accnt_visibility.click_gender()
        self.accnt_visibility.search_accnt_info1(password,
                                                 dayinfo,
                                                 monthinfo,
                                                 yearinfo)
        self.chk_newsletter.click_newsletter()
        self.chk_partner.click_partner()
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

        # Verify 'ACCOUNT CREATED!' and click 'Continue' button
        self.accnt_created.verify_accnt_created_banner()
        self.accnt_created.click_accnt_continue_btn()

        # Verify ' Logged in as username' at top
        self.logged_user.verify_logged_username()

        # Add products to cart
        self.logged_user.click_item1()
        self.logged_user.click_continue_shopping_btn()
        self.logged_user.click_item2()

        # Click 'Cart' button
        go_to_cart_page = self.lp.enterHomepage_Cart_Page()

        # Verify that cart page is displayed
        go_to_cart_page.verify_item1()
        go_to_cart_page.verify_item2()

        # Click Proceed To Checkout
        go_to_cart_page.click_checkout_btn()

        # Verify that the delivery address is same address filled at the time registration of account
        self.accnt_information.verify_address_info(fnames,
                                                   lnames,
                                                   compdet,
                                                   address1,
                                                   state,
                                                   city,
                                                   zipcode,
                                                   countryname,
                                                   mobilenum)
        # Verify that the billing address is same address filled at the time registration of account
        self.accnt_information.verify_address_info_billing(fnames,
                                                           lnames,
                                                           compdet,
                                                           address1,
                                                           state,
                                                           city,
                                                           zipcode,
                                                           countryname,
                                                           mobilenum)

        # Click 'Delete Account' button
        self.logged_user.click_delete_btn()

        # Verify 'ACCOUNT DELETED!' and click 'Continue' button
        self.accnt_deleted.verify_accnt_visible()
        self.accnt_deleted.click_continue_btn()
