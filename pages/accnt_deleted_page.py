import logging

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class AccntDeleted(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ACCOUNT_VISIBLE = "//b[normalize-space()='Account Deleted!']"
    CONTINUE_BTN = "//a[normalize-space()='Continue']"

    def get_accnt_visible(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.ACCOUNT_VISIBLE)

    def get_continue_btn(self):
        return self.driver.find_element(By.XPATH, self.CONTINUE_BTN)

    def verify_accnt_visible(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\account_deleted_banner.png")
        self.log.info(self.get_accnt_visible().text+' is visible')
        assert self.get_accnt_visible().text == "ACCOUNT DELETED!"
        if not (self.get_accnt_visible().text == "ACCOUNT DELETED!"):
            raise AssertionError

    def click_continue_btn(self):
        self.get_continue_btn().click()
