import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SignupPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGIN_BANNER = "//h2[normalize-space()='Login to your account']"
    SIGNUP_BANNER = "//h2[normalize-space()='New User Signup!']"
    NAME_INPUT = "//input[@placeholder='Name']"
    EMAIL_INPUT = "//input[@data-qa='signup-email']"
    LOGIN_EMAIL = "//input[@data-qa='login-email']"
    LOGIN_PASSWORD = "//input[@placeholder='Password']"
    SIGNUP_BTN = "//button[normalize-space()='Signup']"
    LOGIN_BTN = "//button[normalize-space()='Login']"
    INCORRECT_LOGIN_BANNER = "//p[normalize-space()='Your email or password is incorrect!']"
    REGISTERED_SIGNUP_BANNER = "//p[normalize-space()='Email Address already exist!']"
    CART_PAGE = "//a[normalize-space()='Cart']"

    def get_signup_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.SIGNUP_BANNER)

    def get_login_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.LOGIN_BANNER)

    def get_invalid_login_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.INCORRECT_LOGIN_BANNER)

    def get_registered_signup_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.REGISTERED_SIGNUP_BANNER)

    def get_name_input(self):
        return self.driver.find_element(By.XPATH, self.NAME_INPUT)

    def get_cart_page(self):
        return self.driver.find_element(By.XPATH, self.CART_PAGE)

    def get_email_input(self):
        return self.driver.find_element(By.XPATH, self.EMAIL_INPUT)

    def get_login_email_input(self):
        return self.driver.find_element(By.XPATH, self.LOGIN_EMAIL)

    def get_login_password_input(self):
        return self.driver.find_element(By.XPATH, self.LOGIN_PASSWORD)

    def get_signup_btn(self):
        return self.driver.find_element(By.XPATH, self.SIGNUP_BTN)

    def get_login_btn(self):
        return self.driver.find_element(By.XPATH, self.LOGIN_BTN)

    def verify_signup_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\signup_banner.png")
        self.log.info(self.get_signup_banner().text+' is visible')
        assert self.get_signup_banner().text == "New User Signup!"
        if not (self.get_signup_banner().text == "New User Signup!"):
            raise AssertionError

    def verify_login_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\login_banner.png")
        self.log.info(self.get_login_banner().text+' is visible')
        assert self.get_login_banner().text == "Login to your account"
        if not (self.get_login_banner().text == "Login to your account"):
            raise AssertionError

    def verify_invalid_login_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\invalid_login_banner.png")
        self.log.info(self.get_invalid_login_banner().text+' is visible')
        assert self.get_invalid_login_banner().text == "Your email or password is incorrect!"
        if not (self.get_invalid_login_banner().text == "Your email or password is incorrect!"):
            raise AssertionError

    def verify_registered_signup_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\registered_signup_banner.png")
        self.log.info(self.get_registered_signup_banner().text+' is visible')
        assert self.get_registered_signup_banner().text == "Email Address already exist!"
        if not (self.get_registered_signup_banner().text == "Email Address already exist!"):
            raise AssertionError

    def enter_name_input(self, namename):
        self.get_name_input().send_keys(namename)

    def enter_email_input(self, emailemail):
        self.get_email_input().send_keys(emailemail)

    def enter_login_email_input(self, lemail):
        self.get_login_email_input().send_keys(lemail)

    def enter_login_password_input(self, lpassword):
        self.get_login_password_input().send_keys(lpassword)

    def click_signup_btn(self):
        self.get_signup_btn().click()

    def click_login_btn(self):
        self.get_login_btn().click()

    def search_input(self, namename, emailemail):
        self.enter_name_input(namename)
        self.enter_email_input(emailemail)
        self.click_signup_btn()

    def search_login_input(self, lemail, lpassword):
        self.enter_login_email_input(lemail)
        self.enter_login_password_input(lpassword)
        self.click_login_btn()

    def click_cart_btn(self):
        self.get_cart_page().click()
