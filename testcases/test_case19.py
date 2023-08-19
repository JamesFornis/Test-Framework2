import time
import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.products_page import ProductsPage


@pytest.mark.usefixtures("setup")
class TestCase19(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.products = ProductsPage(self.driver)

    @pytest.mark.test_case_19
    def test_case19(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Click on 'Products' button
        go_to_product_page = self.lp.enterHomepage_Products_Page()

        # Verify that Brands are visible on left sidebar
        go_to_product_page.verify_brands()

        # Click on any brand name
        go_to_product_page.click_polo_brand()

        # Verify that user is navigated to brand page and brand products are displayed
        go_to_product_page.verify_polo_brand_banner()

        # On left sidebar, click on any other brand link
        go_to_product_page.click_h_and_m_brand()

        # Verify that user is navigated to that brand page and can see products
        go_to_product_page.verify_h_and_m_brand_banner()
