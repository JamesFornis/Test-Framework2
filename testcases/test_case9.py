import pytest
import unittest
from pages.launch_page import LaunchPage
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestCase9(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    @pytest.mark.test_case_9
    @file_data("../testdata/search_item_data.json")
    def test_case9(self, search_keyword):
        # Launch browser
        # Navigate to url 'http://automationexercise.com'
        # Verify that home page is visible successfully
        # Click on 'Products' button
        go_to_products_page = self.lp.enterHomepage_Products_Page()

        # Verify user is navigated to ALL PRODUCTS page successfully
        go_to_products_page.verify_products_banner()

        # Enter product name in search input and click search button
        go_to_products_page.search_product_input(search_keyword)

        # Verify 'SEARCHED PRODUCTS' is visible
        go_to_products_page.verify_search_products_banner()

        # Verify all the products related to search are visible
        go_to_products_page.verify_search_products_value()
