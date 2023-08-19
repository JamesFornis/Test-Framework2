import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.signup_login_page import SignupPage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TestCasesPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utilities.utils import Utils


class LaunchPage:
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    HOMEPAGE_PAGE = "//a[normalize-space()='Signup / Login']"
    CONTACT_PAGE = "//a[normalize-space()='Contact us']"
    TEST_CASES = "//a[contains(text(),'Test Cases')]"
    PRODUCTS_PAGE = "//a[@href='/products']"
    LAUNCH_PAGE = "//a[normalize-space()='Home']"
    SUBSCRIPTION_BANNER = "//h2[normalize-space()='Subscription']"
    EMAIL_ADDRESS_INPUT = "//input[@id='susbscribe_email']"
    SUBSCRIBE_BTN = "//button[@id='subscribe']"
    SUCCESS_MESSAGE = "//div[@class='footer-widget']//div[@class='row']"
    CART_PAGE = "//body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]"
    VIEW_PRODUCT_BTN = "a[href='/product_details/3']"
    CATEGORIES = "//div[@id='accordian']"
    WOMEN_CATEGORY = "//a[normalize-space()='Women']"
    RECOMMENDED_ITEMS = "//h2[normalize-space()='recommended items']"
    ADD_TO_CART = "//div[@class='item active']//div[1]//div[1]//div[1]//div[1]//a[1]"
    VIEW_CART_BTN = "//u[normalize-space()='View Cart']"
    UPWARD_ARROW = "//i[@class='fa fa-angle-up']"
    FULL_FLEDGED_BANNER = "//div[@class='item active']//h2[contains(text(),'Full-Fledged practice website for Automation Engin')]"
    BODY = 'body'

    def getHompagePage(self):
        return self.driver.find_element(By.XPATH, self.HOMEPAGE_PAGE)

    def getLaunchPage(self):
        return self.driver.find_element(By.XPATH, self.LAUNCH_PAGE)

    def getContactPage(self):
        return self.driver.find_element(By.XPATH, self.CONTACT_PAGE)

    def get_full_fledged_banner(self):
        return self.driver.find_element(By.XPATH, self.FULL_FLEDGED_BANNER)

    def get_upward_arrow(self):
        return self.driver.find_element(By.XPATH, self.UPWARD_ARROW)

    def getTestCasesPage(self):
        return self.driver.find_element(By.XPATH, self.TEST_CASES)

    def getCartPage(self):
        return self.driver.find_element(By.XPATH, self.CART_PAGE)

    def getProductsPage(self):
        return self.driver.find_element(By.XPATH, self.PRODUCTS_PAGE)

    def get_add_to_cart_btn(self):
        return self.driver.find_element(By.XPATH, self.ADD_TO_CART)

    def get_view_cart_btn(self):
        return self.driver.find_element(By.XPATH, self.VIEW_CART_BTN)

    def getSubscriptionBanner(self):
        return self.driver.find_element(By.XPATH, self.SUBSCRIPTION_BANNER)

    def getEmailInput(self):
        return self.driver.find_element(By.XPATH, self.EMAIL_ADDRESS_INPUT)

    def getCategories(self):
        return self.driver.find_element(By.XPATH, self.CATEGORIES)

    def get_women_category(self):
        return self.driver.find_element(By.XPATH, self.WOMEN_CATEGORY)

    def get_recommended_items(self):
        return self.driver.find_element(By.XPATH, self.RECOMMENDED_ITEMS)

    def getSubscribeBtn(self):
        return self.driver.find_element(By.XPATH, self.SUBSCRIBE_BTN)

    def getViewProductBtn(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.VIEW_PRODUCT_BTN)

    def getSuccessMessage(self):
        return self.driver.find_element(By.XPATH, self.SUCCESS_MESSAGE)

    def get_scroll_up(self):
        return self.driver.find_element(By.TAG_NAME, self.BODY)

    def verify_subscription_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\subscription_banner.png")
        self.log.info(self.getSubscriptionBanner().text+' is visible')
        assert self.getSubscriptionBanner().text == "SUBSCRIPTION"
        if not (self.getSubscriptionBanner().text == "SUBSCRIPTION"):
            raise AssertionError

    def verify_full_fledged_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\full_fledged_banner.png")
        self.log.info(self.get_full_fledged_banner().text+' is visible')
        assert self.get_full_fledged_banner().text == "Full-Fledged practice website for Automation Engineers"
        if not (self.get_full_fledged_banner().text == "Full-Fledged practice website for Automation Engineers"):
            raise AssertionError

    def verify_recommended_items_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\recommended_items_banner.png")
        self.log.info(self.get_recommended_items().text+' is visible')
        assert self.get_recommended_items().text == "RECOMMENDED ITEMS"
        if not (self.get_recommended_items().text == "RECOMMENDED ITEMS"):
            raise AssertionError

    def verify_success_message(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\success_msg_banner.png")
        self.log.info(self.getSuccessMessage().text + ' is visible')

    def enterLaunch_Page(self):
        self.log.info("Homepage is visible")
        self.getLaunchPage().click()

    def enterHomepage_Page(self):
        self.log.info("Homepage is visible")
        self.getHompagePage().click()
        go_to_signup_page = SignupPage(self.driver)
        return go_to_signup_page

    def enterHomepage_ContactUs_Page(self):
        self.log.info("Homepage is visible")
        self.getContactPage().click()
        go_to_contact_us_page = ContactUsPage(self.driver)
        return go_to_contact_us_page

    def enterHomepage_TestCases_Page(self):
        self.log.info("Homepage is visible")
        self.getTestCasesPage().click()
        go_to_test_cases_page = TestCasesPage(self.driver)
        return go_to_test_cases_page

    def enterHomepage_Cart_Page(self):
        self.log.info("Homepage is visible")
        self.getCartPage().click()
        go_to_cart_page = CartPage(self.driver)
        return go_to_cart_page

    def enterHomepage_Products_Page(self):
        self.log.info("Homepage is visible")
        self.getProductsPage().click()
        time.sleep(3)
        go_to_products_page = ProductsPage(self.driver)
        return go_to_products_page

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def scroll_up(self):
        self.get_scroll_up().send_keys(Keys.HOME)

    def input_email_address(self, email):
        self.getEmailInput().send_keys(email)

    def subscribe_btn(self):
        self.getSubscribeBtn().click()

    def search_subscribe(self, email):
        self.input_email_address(email)
        self.subscribe_btn()

    def scroll_and_click_view_product_btn(self):
        viewProductBtn = self.getViewProductBtn()
        self.driver.execute_script("arguments[0].scrollIntoView();", viewProductBtn)
        viewProductBtn.click()

    def verify_categories(self):
        self.log.info(self.getCategories().is_displayed())

    def click_women_category(self):
        women_category = self.get_women_category()
        self.driver.execute_script("arguments[0].scrollIntoView();", women_category)
        women_category.click()

    def click_add_to_cart_btn(self):
        add_to_cart = self.get_add_to_cart_btn()
        self.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)
        add_to_cart.click()

    def click_view_cart_btn(self):
        self.get_view_cart_btn().click()

    def click_upward_arrow_btn(self):
        upward_arrow = self.get_upward_arrow()
        self.driver.execute_script("arguments[0].scrollIntoView();", upward_arrow)
        upward_arrow.click()
