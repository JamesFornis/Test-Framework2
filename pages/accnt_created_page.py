import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class AccntCreated(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ACCNT_CREATED = "//b[normalize-space()='Account Created!']"
    ACCNT_CONTINUE_BTN = "//a[normalize-space()='Continue']"

    def get_accnt_created_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.ACCNT_CREATED)

    def get_accnt_continue_btn(self):
        return self.driver.find_element(By.XPATH, self.ACCNT_CONTINUE_BTN)

    def verify_accnt_created_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\account_created_banner.png")
        self.log.info(self.get_accnt_created_banner().text+' is visible')
        assert self.get_accnt_created_banner().text == "ACCOUNT CREATED!"
        if not (self.get_accnt_created_banner().text == "ACCOUNT CREATED!"):
            raise AssertionError

    def click_accnt_continue_btn(self):
        self.get_accnt_continue_btn().click()
