import pytest
import unittest
from pages.launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestCase8(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    @pytest.mark.test_case_8
    def test_case8(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click on 'Products' button
        go_to_products_page = self.lp.enterHomepage_Products_Page()

        # Verify user is navigated to ALL PRODUCTS page successfully
        # The products list is visible
        go_to_products_page.verify_products_banner()

        # Click on 'View Product' of first product
        # User is landed to product detail page
        go_to_products_page.click_first_product_link()

        # Verify that detail is visible: product name, category, price, availability, condition, brand
        go_to_products_page.verify_first_product_name_label()
        go_to_products_page.verify_first_product_category_label()
        go_to_products_page.verify_first_product_price_label()
        go_to_products_page.verify_first_product_availability_label()
        go_to_products_page.verify_first_product_condition_label()
        go_to_products_page.verify_first_product_brand_label()
