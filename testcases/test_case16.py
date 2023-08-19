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
class TestCase16(unittest.TestCase):

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

    @pytest.mark.test_case_16
    @file_data("../testdata/logout_data.json")
    def test_case16(self, logout_email, logout_password, card_name, card_num, cvc, exp_month, exp_year, search_keyword):
        # launch browser and open url
        # Verify that home page is visible successfully
        # Click on 'Signup / Login' button
        go_to_signup_page = self.lp.enterHomepage_Page()

        # Fill email, password and click 'Login' button
        go_to_signup_page.search_login_input(logout_email,
                                             logout_password)

        # Verify 'Logged in as username' at top
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
