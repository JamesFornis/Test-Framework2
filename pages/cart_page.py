import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class CartPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GET_SUBSCRIPTION_BANNER = "//h2[normalize-space()='Subscription']"
    CART_EMAIL = "//input[@id='susbscribe_email']"
    CART_BTN = "//button[@id='subscribe']"
    SUCCESS_MESSAGE = "//div[@class='alert-success alert']"
    CART_ITEM1 = "//a[normalize-space()='Blue Top']"
    CART_ITEM2 = "//a[normalize-space()='Men Tshirt']"
    PRICE1 = "//p[normalize-space()='Rs. 500']"
    PRICE2 = "//td[@class='cart_price']//p[contains(text(),'Rs. 400')]"
    QUANTITY1 = "//button[normalize-space()='1']"
    QUANTITY2 = "//button[normalize-space()='1']"
    TOTAL1 = "//p[normalize-space()='Rs. 500']"
    TOTAL2 = "//p[@class='cart_total_price'][normalize-space()='Rs. 400']"
    VIEW_PRODUCT_QUANTITY = "//button[normalize-space()='4']"
    PROCEED_CHECKOUT_BTN = "//a[normalize-space()='Proceed To Checkout']"
    REGISTER_LOGIN = "//u[normalize-space()='Register / Login']"
    ADDRESS_DETAILS = "//h2[normalize-space()='Address Details']"
    REVIEW_YOUR_ORDER = "//h2[normalize-space()='Review Your Order']"
    COMMENT_TEXT_AREA = "//textarea[@name='message']"
    PLACE_ORDER_BTN = "//a[normalize-space()='Place Order']"
    X_BTN = "//tr[@id='product-1']//a[@class='cart_quantity_delete']"
    SIGNUPLOGIN_BTN = "//a[normalize-space()='Signup / Login']"
    CART_ITEM = "//a[normalize-space()='Stylish Dress']"

    def scroll_down_cart(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def get_subscription_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.GET_SUBSCRIPTION_BANNER)

    def get_address_details_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.ADDRESS_DETAILS)

    def get_review_your_order_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.REVIEW_YOUR_ORDER)

    def get_view_product_quantity(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.VIEW_PRODUCT_QUANTITY)

    def get_item1(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.CART_ITEM1)

    def get_item2(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.CART_ITEM2)

    def get_price1(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.PRICE1)

    def get_price2(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.PRICE2)

    def get_quantity1(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.QUANTITY1)

    def get_quantity2(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.QUANTITY2)

    def get_total1(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.TOTAL1)

    def get_total2(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.TOTAL2)

    def get_comment_text_area(self):
        return self.driver.find_element(By.XPATH, self.COMMENT_TEXT_AREA)

    def get_cart_item(self):
        return self.driver.find_element(By.XPATH, self.CART_ITEM)

    def get_x_btn(self):
        return self.driver.find_element(By.XPATH, self.X_BTN)

    def get_signup_login_btn(self):
        return self.driver.find_element(By.XPATH, self.SIGNUPLOGIN_BTN)

    def get_place_order_btn(self):
        return self.driver.find_element(By.XPATH, self.PLACE_ORDER_BTN)

    def get_cart_email(self):
        return self.driver.find_element(By.XPATH, self.CART_EMAIL)

    def get_cart_email_btn(self):
        return self.driver.find_element(By.XPATH, self.CART_BTN)

    def get_check_out_btn(self):
        return self.driver.find_element(By.XPATH, self.PROCEED_CHECKOUT_BTN)

    def get_register_login_btn(self):
        return self.driver.find_element(By.XPATH, self.REGISTER_LOGIN)

    def get_cart_success_message(self):
        return self.driver.find_element(By.XPATH, self.SUCCESS_MESSAGE)

    def verify_cart_subscription_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\cart_subscription_banner.png")
        self.log.info(self.get_subscription_banner().text+' is visible')
        assert self.get_subscription_banner().text == "SUBSCRIPTION"
        if not (self.get_subscription_banner().text == "SUBSCRIPTION"):
            raise AssertionError

    def verify_address_detail_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\address_detail_banner.png")
        self.log.info(self.get_address_details_banner().text+' is visible')
        assert self.get_address_details_banner().text == "Address Details"
        if not (self.get_address_details_banner().text == "Address Details"):
            raise AssertionError

    def verify_review_your_order_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\review_your_order_banner.png")
        review_your_order = self.get_review_your_order_banner()
        self.driver.execute_script("arguments[0].scrollIntoView();", review_your_order)
        self.log.info(self.get_review_your_order_banner().text+' is visible')
        assert self.get_review_your_order_banner().text == "Review Your Order"
        if not (self.get_review_your_order_banner().text == "Review Your Order"):
            raise AssertionError

    def verify_item1(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\cart_item1.png")
        self.log.info(self.get_item1().text+' is visible')
        assert self.get_item1().text == "Blue Top"
        if not (self.get_item1().text == "Blue Top"):
            raise AssertionError

    def verify_item2(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\cart_item2.png")
        self.log.info(self.get_item2().text+' is visible')
        assert self.get_item2().text == "Men Tshirt"
        if not (self.get_item2().text == "Men Tshirt"):
            raise AssertionError

    def verify_price1(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\price_item1.png")
        self.log.info(self.get_price1().text+' is visible')
        assert self.get_price1().text == "Rs. 500"
        if not (self.get_price1().text == "Rs. 500"):
            raise AssertionError

    def verify_price2(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\price_item2.png")
        self.log.info(self.get_price2().text+' is visible')
        assert self.get_price2().text == "Rs. 400"
        if not (self.get_price2().text == "Rs. 400"):
            raise AssertionError

    def verify_quantity1(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\quantity_item1.png")
        self.log.info(self.get_quantity1().text+' is visible')
        assert self.get_quantity1().text == "1"
        if not (self.get_quantity1().text == "1"):
            raise AssertionError

    def verify_quantity2(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\quantity_item2.png")
        self.log.info(self.get_quantity2().text+' is visible')
        assert self.get_quantity2().text == "1"
        if not (self.get_quantity2().text == "1"):
            raise AssertionError

    def verify_total1(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\total_price_item1.png")
        self.log.info(self.get_total1().text+' is visible')
        assert self.get_total1().text == "Rs. 500"
        if not (self.get_total1().text == "Rs. 500"):
            raise AssertionError

    def verify_total2(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\total_price_item2.png")
        self.log.info(self.get_total2().text+' is visible')
        assert self.get_total2().text == "Rs. 400"
        if not (self.get_total2().text == "Rs. 400"):
            raise AssertionError

    def verify_view_product_qty(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\view_product_qty.png")
        self.log.info(self.get_view_product_quantity().text+' is visible')
        assert self.get_view_product_quantity().text == "4"
        if not (self.get_view_product_quantity().text == "4"):
            raise AssertionError

    def verify_cart_success_message(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\cart_success_msg_banner.png")
        self.log.info(self.get_cart_success_message().text + ' is visible')

    def input_cart_email_address(self, email):
        self.get_cart_email().send_keys(email)

    def subscribe_cart_btn(self):
        self.get_cart_email_btn().click()

    def search_cart_subscribe(self, email):
        self.input_cart_email_address(email)
        self.subscribe_cart_btn()

    def verify_cart(self):
        self.verify_price1()
        self.verify_price2()
        self.verify_quantity1()
        self.verify_quantity2()
        self.verify_total1()
        self.verify_total2()

    def click_checkout_btn(self):
        self.get_check_out_btn().click()

    def click_register_login_btn(self):
        self.get_register_login_btn().click()

    def input_comment_text_area(self):
        time.sleep(3)
        self.get_comment_text_area().click()
        self.get_comment_text_area().send_keys(self.get_item1().text, self.get_item2().text)

    def click_place_order_btn(self):
        place_order = self.get_place_order_btn()
        self.driver.execute_script("arguments[0].scrollIntoView();", place_order)
        place_order.click()

    def click_x_btn(self):
        self.get_x_btn().click()

    def verify_item(self):
        self.log.info(self.get_item1().is_displayed())

    def verify_item_tshirt(self):
        self.log.info(self.get_item2().is_displayed())

    def click_signup_login_btn(self):
        self.get_signup_login_btn().click()

    def verify_cart_item(self):
        self.log.info(self.get_cart_item().is_displayed())
