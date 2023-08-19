import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class ContactUsPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GET_IN_TOUCH_BANNER = "//h2[normalize-space()='Get In Touch']"
    NAME_INPUT = "//input[@placeholder='Name']"
    EMAIL_INPUT = "//input[@placeholder='Email']"
    SUBJECT_INPUT = "//input[@placeholder='Subject']"
    MESSAGE_INPUT = "//textarea[@id='message']"
    UPLOAD_FILE_BTN = "//input[@name='upload_file']"
    SUBMIT_BTN = "//input[@name='submit']"
    SUCCESS_BANNER = "//div[@class='status alert alert-success']"
    HOME_BTN = "//span[normalize-space()='Home']"

    def get_get_in_touch_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.GET_IN_TOUCH_BANNER)

    def get_success_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.SUCCESS_BANNER)

    def get_name_input(self):
        return self.driver.find_element(By.XPATH, self.NAME_INPUT)

    def get_email_input(self):
        return self.driver.find_element(By.XPATH, self.EMAIL_INPUT)

    def get_subject_input(self):
        return self.driver.find_element(By.XPATH, self.SUBJECT_INPUT)

    def get_message_input(self):
        return self.driver.find_element(By.XPATH, self.MESSAGE_INPUT)

    def get_upload_file_btn(self):
        return self.driver.find_element(By.XPATH, self.UPLOAD_FILE_BTN)

    def get_submit_btn(self):
        return self.driver.find_element(By.XPATH, self.SUBMIT_BTN)

    def get_home_btn(self):
        return self.driver.find_element(By.XPATH, self.HOME_BTN)

    def verify_get_in_touch_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\get_in_touch_banner.png")
        self.log.info(self.get_get_in_touch_banner().text+' is visible')
        assert self.get_get_in_touch_banner().text == "GET IN TOUCH"
        if not (self.get_get_in_touch_banner().text == "GET IN TOUCH"):
            raise AssertionError

    def verify_success_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\success_banner.png")
        self.log.info(self.get_success_banner().text+' is visible')
        assert self.get_success_banner().text == "Success! Your details have been submitted successfully."
        if not (self.get_success_banner().text == "Success! Your details have been submitted successfully."):
            raise AssertionError

    def enter_name_input(self, contact_name):
        self.get_name_input().send_keys(contact_name)

    def enter_email_input(self, contact_email):
        self.get_email_input().send_keys(contact_email)

    def enter_subject_input(self, contact_subject):
        self.get_subject_input().send_keys(contact_subject)

    def enter_message_input(self, contact_message):
        self.get_message_input().send_keys(contact_message)

    def search_contact_input(self, contact_name, contact_email, contact_subject, contact_message):
        self.enter_name_input(contact_name)
        self.enter_email_input(contact_email)
        self.enter_subject_input(contact_subject)
        self.enter_message_input(contact_message)

    def click_upload_file_btn(self):
        self.get_upload_file_btn().send_keys("C:\\Users\\James Fornis\\Desktop\\task.jpg")

    def click_submit_btn(self):
        self.get_submit_btn().click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)

    def click_home_btn(self):
        self.get_home_btn().click()
