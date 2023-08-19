import time
import pytest
import unittest
from pages.launch_page import LaunchPage
from pages.products_page import ProductsPage


@pytest.mark.usefixtures("setup")
class TestCase18(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.products = ProductsPage(self.driver)

    @pytest.mark.test_case_18
    def test_case18(self):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        self.lp.enterLaunch_Page()

        # Verify that categories are visible on left sidebar
        self.lp.verify_categories()

        # Click on 'Women' category
        self.lp.click_women_category()

        # Click on any category link under 'Women' category, for example: Dress
        self.products.click_tops_category()

        # Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
        self.products.verify_tops_product_banner()

        # On left sidebar, click on any sub-category link of 'Men' category
        self.products.click_men_category()
        self.products.click_tshirt_category()

        # Verify that user is navigated to that category page
        self.products.verify_tshirt_product_banner()
