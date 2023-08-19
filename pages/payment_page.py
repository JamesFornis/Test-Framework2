import logging
import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class PaymentPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    NAME_ON_CARD = "//input[@name='name_on_card']"
    CARD_NUMBER = "//input[@name='card_number']"
    CVC = "//input[@placeholder='ex. 311']"
    EXP_MONTH = "//input[@placeholder='MM']"
    EXP_YEAR = "//input[@placeholder='YYYY']"
    PAY_AND_CONFIRM_ORDER = "//button[@id='submit']"

    def get_name_on_card(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.NAME_ON_CARD)

    def get_card_number(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.CARD_NUMBER)

    def get_cvc(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.CVC)

    def get_exp_month(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.EXP_MONTH)

    def get_exp_year(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.EXP_YEAR)

    def get_pay_and_confirm_btn(self):
        return self.driver.find_element(By.XPATH, self.PAY_AND_CONFIRM_ORDER)

    def input_details_on_card(self, card_name, card_num, cvc, exp_month, exp_year):
        self.get_name_on_card().send_keys(card_name)
        self.get_card_number().send_keys(card_num)
        self.get_cvc().send_keys(cvc)
        self.get_exp_month().send_keys(exp_month)
        self.get_exp_year().send_keys(exp_year)

    def click_pay_and_confirm_order_btn(self):
        pay_and_confirm_btn = self.get_pay_and_confirm_btn()
        self.driver.execute_script("arguments[0].scrollIntoView();", pay_and_confirm_btn)
        pay_and_confirm_btn.click()

