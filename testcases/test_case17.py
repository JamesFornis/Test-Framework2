import time
import pytest
import unittest
from pages.accnt_created_page import AccntCreated
from pages.accnt_deleted_page import AccntDeleted
from pages.accnt_info_page import AccntInfo
from pages.launch_page import LaunchPage
from pages.logged_page import LoggedPage
from pages.signup_login_page import SignupPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage


@pytest.mark.usefixtures("setup")
class TestCase17(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.sp = SignupPage(self.driver)
        self.payment = PaymentPage(self.driver)
        self.accnt_visibility = AccntInfo(self.driver)
        self.chk_newsletter = AccntInfo(self.driver)
        self.chk_partner = AccntInfo(self.driver)
        self.accnt_information = AccntInfo(self.driver)
        self.accnt_created = AccntCreated(self.driver)
        self.logged_user = LoggedPage(self.driver)
        self.accnt_deleted = AccntDeleted(self.driver)
        self.products = ProductsPage(self.driver)

    @pytest.mark.test_case_17
    def test_case17(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        go_to_product_page = self.products

        # Add products to cart
        go_to_product_page.scroll_and_click_add_to_cart_btn()
        go_to_product_page.click_continue_shopping_btn()
        go_to_product_page.click_add_to_cart2_btn()

        # Click 'Cart' button
        go_to_cart_page = self.lp.enterHomepage_Cart_Page()

        # Verify that cart page is displayed
        go_to_cart_page.verify_item1()
        go_to_cart_page.verify_item2()

        # Click 'X' button corresponding to particular product
        go_to_cart_page.click_x_btn()

        # Verify that product is removed from the cart
        go_to_cart_page.verify_item()
