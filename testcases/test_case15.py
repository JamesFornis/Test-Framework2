import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.accnt_info_page import AccntInfo
from pages.accnt_created_page import AccntCreated
from pages.logged_page import LoggedPage
from pages.accnt_deleted_page import AccntDeleted
from ddt import ddt, file_data
from pages.payment_page import PaymentPage


@pytest.mark.usefixtures("setup")
@ddt
class TestCase15(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.payment = PaymentPage(self.driver)
        self.accnt_visibility = AccntInfo(self.driver)
        self.chk_newsletter = AccntInfo(self.driver)
        self.chk_partner = AccntInfo(self.driver)
        self.accnt_information = AccntInfo(self.driver)
        self.accnt_created = AccntCreated(self.driver)
        self.logged_user = LoggedPage(self.driver)
        self.accnt_deleted = AccntDeleted(self.driver)

    @pytest.mark.test_case_15
    @file_data("../testdata/data.json")
    def test_case15(self, name, email, password, dayinfo, monthinfo, yearinfo, fnames, lnames, compdet, address1, address2, countryname, state, city, zipcode, mobilenum, card_name, card_num, cvc, exp_month, exp_year):
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

        # Verify Address Details and Review Your Order
        go_to_cart_page.verify_address_detail_banner()
        go_to_cart_page.verify_review_your_order_banner()

        # Enter description in comment text area and click 'Place Order'
        go_to_cart_page.input_comment_text_area()
        go_to_cart_page.click_place_order_btn()

        # Enter payment details: Name on Card, Card Number, CVC, Expiration date
        self.payment.input_details_on_card(card_name,
                                           card_num,
                                           cvc,
                                           exp_month,
                                           exp_year)
        # Click 'Pay and Confirm Order' button
        # Verify success message 'Your order has been placed successfully!'
        self.payment.click_pay_and_confirm_order_btn()

        # Click 'Delete Account' button
        self.logged_user.click_delete_btn()

        # Verify 'ACCOUNT DELETED!' and click 'Continue' button
        self.accnt_deleted.verify_accnt_visible()
        self.accnt_deleted.click_continue_btn()
