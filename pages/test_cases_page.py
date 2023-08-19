import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class TestCasesPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GET_TEST_CASES_BANNER = "//b[normalize-space()='Test Cases']"

    def get_test_cases_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.GET_TEST_CASES_BANNER)

    def verify_test_cases_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\test_cases_banner.png")
        self.log.info(self.get_test_cases_banner().text+' is visible')
        assert self.get_test_cases_banner().text == "TEST CASES"
        if not (self.get_test_cases_banner().text == "TEST CASES"):
            raise AssertionError
