import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils
from pages.signup_login_page import SignupPage


class LoggedPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGGED_USERNAME = "//li[10]//a[1]"
    USERNAME = "ul[class='nav navbar-nav'] li a b"
    DELETE_BTN = "//a[normalize-space()='Delete Account']"
    LOGOUT_BTN = "//a[normalize-space()='Logout']"
    ADD_ITEM1 = "//body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/div[3]/div[1]/div[1]/div[1]/a[1]"
    ADD_ITEM2 = "(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[3]"
    CONTINUE_SHOPPING_BTN = "//button[normalize-space()='Continue Shopping']"
    DOWNLOAD_INVOICE_BTN = "//a[normalize-space()='Download Invoice']"
    CONTINUE_INVOICE_BTN = "//a[normalize-space()='Continue']"

    def get_logged_username(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.LOGGED_USERNAME)

    def get_username_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.USERNAME)

    def get_continue_invoice_btn(self):
        return self.driver.find_element(By.XPATH, self.CONTINUE_INVOICE_BTN)

    def get_download_invoice_btn(self):
        return self.driver.find_element(By.XPATH, self.DOWNLOAD_INVOICE_BTN)

    def get_item1(self):
        return self.driver.find_element(By.XPATH, self.ADD_ITEM1)

    def get_item2(self):
        return self.driver.find_element(By.XPATH, self.ADD_ITEM2)

    def get_continue_shopping_btn(self):
        return self.driver.find_element(By.XPATH, self.CONTINUE_SHOPPING_BTN)

    def get_delete_btn(self):
        return self.driver.find_element(By.XPATH, self.DELETE_BTN)

    def get_logout_btn(self):
        return self.driver.find_element(By.XPATH, self.LOGOUT_BTN)

    def verify_logged_username(self):
        time.sleep(3)
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\logged_username.png")
        self.log.info(self.get_logged_username().text)
        log_username = self.get_username_label().text
        assert self.get_logged_username().text == "Logged in as "+log_username
        if not (self.get_logged_username().text == "Logged in as "+log_username):
            raise AssertionError

    def click_delete_btn(self):
        self.get_delete_btn().click()

    def click_logout_btn(self):
        self.get_logout_btn().click()

    def click_item1(self):
        addItem1 = self.get_item1()
        self.driver.execute_script("arguments[0].scrollIntoView();", addItem1)
        addItem1.click()

    def click_continue_shopping_btn(self):
        self.get_continue_shopping_btn().click()

    def click_item2(self):
        self.get_item2().click()

    def click_download_invoice_btn(self):
        self.get_download_invoice_btn().click()

    def click_continue_invoice_btn(self):
        time.sleep(3)
        self.get_continue_invoice_btn().click()
