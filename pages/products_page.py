import logging
import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class ProductsPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GET_PRODUCTS_BANNER = "//h2[normalize-space()='All Products']"
    FIRST_PRODUCTS = "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]"
    FIRST_PRODUCT_NAME = "//h2[normalize-space()='Blue Top']"
    FIRST_PRODUCT_CATEGORY = "//p[normalize-space()='Category: Women > Tops']"
    FIRST_PRODUCT_PRICE = "//span[normalize-space()='Rs. 500']"
    FIRST_PRODUCT_AVAILABILITY = "//b[normalize-space()='Availability:']"
    FIRST_PRODUCT_CONDITION = "//b[normalize-space()='Condition:']"
    FIRST_PRODUCT_BRAND = "//b[normalize-space()='Brand:']"
    SEARCH_PRODUCT = "//input[@id='search_product']"
    SEARCH_PRODUCT_BTN = "//button[@id='submit_search']"
    SEARCH_PRODUCT_BANNER = "//h2[normalize-space()='Searched Products']"
    SEARCH_PRODUCT_RESULT = "div[class='productinfo text-center'] p"
    ADD_TO_CART_BTN = "//body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/div[2]/div[1]/div[1]/div[1]/a[1]"
    CONTINUE_SHOPPING_BTN = "//button[normalize-space()='Continue Shopping']"
    ADD_TO_CART2_BTN = "(//a[contains(text(),'Add to cart')])[3]"
    VIEW_PRODUCT = "//h2[normalize-space()='Sleeveless Dress']"
    PRODUCT_QTY = "quantity"
    VIEW_PRODUCT_ADD_TO_CART = "//button[normalize-space()='Add to cart']"
    VIEW_CART = "//u[normalize-space()='View Cart']"
    TOPS_CATEGORY = "//a[normalize-space()='Tops']"
    TOPS_PRODUCT_BANNER = "//h2[normalize-space()='Women - Tops Products']"
    MEN_CATEGORY = "//a[normalize-space()='Men']"
    TSHIRT_CATEGORY = "//a[normalize-space()='Tshirts']"
    TSHIRT_PRODUCT_BANNER = "//h2[normalize-space()='Men - Tshirts Products']"
    BRANDS = "//div[@class='brands-name']"
    POLO_BRAND = "//a[@href='/brand_products/Polo']"
    POLO_BRAND_BANNER = "//h2[normalize-space()='Brand - Polo Products']"
    H_AND_M_BRAND = "//a[@href='/brand_products/H&M']"
    H_AND_M_BRAND_BANNER = "//h2[normalize-space()='Brand - H&M Products']"
    MEN_TSHIRT = "//div[@class='productinfo text-center']//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart']"
    VIEW_PRODUCT_BTN = "a[href='/product_details/1']"
    WRITE_YOUR_REVIEW_BANNER = "//a[normalize-space()='Write Your Review']"
    REVIEW_NAME = "//input[@id='name']"
    REVIEW_EMAIL = "//input[@id='email']"
    REVIEW_INPUT = "//textarea[@id='review']"
    REVIEW_SUBMIT_BTN = "//button[@id='button-review']"
    THANKS_FOR_REVIEW_BANNER = "//span[normalize-space()='Thank you for your review.']"

    def get_products_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.GET_PRODUCTS_BANNER)

    def get_thanks_for_review_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.THANKS_FOR_REVIEW_BANNER)

    def get_search_product_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.SEARCH_PRODUCT_BANNER)

    def get_write_your_review_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.WRITE_YOUR_REVIEW_BANNER)

    def get_search_product_result(self):
        return self.wait_element_to_be_clickable(By.CSS_SELECTOR, self.SEARCH_PRODUCT_RESULT)

    def get_brands(self):
        return self.driver.find_element(By.XPATH, self.BRANDS)

    def get_review_name(self):
        return self.driver.find_element(By.XPATH, self.REVIEW_NAME)

    def get_review_email(self):
        return self.driver.find_element(By.XPATH, self.REVIEW_EMAIL)

    def get_review_input(self):
        return self.driver.find_element(By.XPATH, self.REVIEW_INPUT)

    def get_review_submit_btn(self):
        return self.driver.find_element(By.XPATH, self.REVIEW_SUBMIT_BTN)

    def get_view_product_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.VIEW_PRODUCT_BTN)

    def get_h_and_m_brand_banner(self):
        return self.driver.find_element(By.XPATH, self.H_AND_M_BRAND_BANNER)

    def get_tops_category(self):
        return self.driver.find_element(By.XPATH, self.TOPS_CATEGORY)

    def get_men_tshirt(self):
        return self.driver.find_element(By.XPATH, self.MEN_TSHIRT)

    def get_polo_brand_banner(self):
        return self.driver.find_element(By.XPATH, self.POLO_BRAND_BANNER)

    def get_polo_brand(self):
        return self.driver.find_element(By.XPATH, self.POLO_BRAND)

    def get_h_and_m_brand(self):
        return self.driver.find_element(By.XPATH, self.H_AND_M_BRAND)

    def get_first_product_link(self):
        return self.driver.find_element(By.XPATH, self.FIRST_PRODUCTS)

    def get_tshirt_product_banner(self):
        return self.driver.find_element(By.XPATH, self.TSHIRT_PRODUCT_BANNER)

    def get_men_category(self):
        return self.driver.find_element(By.XPATH, self.MEN_CATEGORY)

    def get_tshirt_category(self):
        return self.driver.find_element(By.XPATH, self.TSHIRT_CATEGORY)

    def get_tops_product_banner(self):
        return self.driver.find_element(By.XPATH, self.TOPS_PRODUCT_BANNER)

    def get_view_cart_link(self):
        return self.driver.find_element(By.XPATH, self.VIEW_CART)

    def get_add_to_cart_btn(self):
        return self.driver.find_element(By.XPATH, self.ADD_TO_CART_BTN)

    def get_view_product_add_to_cart_btn(self):
        return self.driver.find_element(By.XPATH, self.VIEW_PRODUCT_ADD_TO_CART)

    def get_add_to_cart2_btn(self):
        return self.driver.find_element(By.XPATH, self.ADD_TO_CART2_BTN)

    def get_product_qty(self):
        return self.driver.find_element(By.ID, self.PRODUCT_QTY)

    def get_continue_shopping_btn(self):
        return self.driver.find_element(By.XPATH, self.CONTINUE_SHOPPING_BTN)

    def get_view_product_label(self):
        return self.driver.find_element(By.XPATH, self.VIEW_PRODUCT)

    def get_first_product_name_label(self):
        return self.driver.find_element(By.XPATH, self.FIRST_PRODUCT_NAME)

    def get_first_product_category_label(self):
        return self.driver.find_element(By.XPATH, self.FIRST_PRODUCT_CATEGORY)

    def get_first_product_price_label(self):
        return self.driver.find_element(By.XPATH, self.FIRST_PRODUCT_PRICE)

    def get_first_product_availability_label(self):
        return self.driver.find_element(By.XPATH, self.FIRST_PRODUCT_AVAILABILITY)

    def get_first_product_condition_label(self):
        return self.driver.find_element(By.XPATH, self.FIRST_PRODUCT_CONDITION)

    def get_first_product_brand_label(self):
        return self.driver.find_element(By.XPATH, self.FIRST_PRODUCT_BRAND)

    def get_search_product(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_PRODUCT)

    def get_search_product_value(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_PRODUCT).get_attribute("value")

    def get_search_product_btn(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_PRODUCT_BTN)

    def verify_products_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\products_banner.png")
        self.log.info(self.get_products_banner().text+' is visible')
        assert self.get_products_banner().text == "ALL PRODUCTS"
        if not (self.get_products_banner().text == "ALL PRODUCTS"):
            raise AssertionError

    def verify_thanks_for_review_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\thanks_for_review_banner.png")
        self.log.info(self.get_thanks_for_review_banner().text+' is visible')
        assert self.get_thanks_for_review_banner().text == "Thank you for your review."
        if not (self.get_thanks_for_review_banner().text == "Thank you for your review."):
            raise AssertionError

    def verify_write_your_review_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\write_your_review_banner.png")
        self.log.info(self.get_write_your_review_banner().text+' is visible')
        assert self.get_write_your_review_banner().text == "Write Your Review"
        if not (self.get_write_your_review_banner().text == "Write Your Review"):
            raise AssertionError

    def verify_search_products_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\search_products_banner.png")
        self.log.info(self.get_search_product_banner().text+' is visible')
        assert self.get_search_product_banner().text == "SEARCHED PRODUCTS"
        if not (self.get_search_product_banner().text == "SEARCHED PRODUCTS"):
            raise AssertionError

    def verify_search_products_value(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\search_products_result.png")
        self.log.info(self.get_search_product_result().text+' is visible')
        assert self.get_search_product_result().text == self.get_search_product_value()
        if not (self.get_search_product_result().text == self.get_search_product_value()):
            raise AssertionError

    def click_first_product_link(self):
        self.get_first_product_link().click()

    def verify_view_product_name_label(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\view_product_name_label.png")
        self.log.info(self.get_view_product_label().text+' is visible')
        assert self.get_view_product_label().text == "Sleeveless Dress"
        if not (self.get_view_product_label().text == "Sleeveless Dress"):
            raise AssertionError

    def verify_first_product_name_label(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\first_product_name_label.png")
        self.log.info(self.get_first_product_name_label().text+' is visible')
        assert self.get_first_product_name_label().text == "Blue Top"
        if not (self.get_first_product_name_label().text == "Blue Top"):
            raise AssertionError

    def verify_first_product_category_label(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\first_product_category_label.png")
        self.log.info(self.get_first_product_category_label().text+' is visible')
        assert self.get_first_product_category_label().text == "Category: Women > Tops"
        if not (self.get_first_product_category_label().text == "Category: Women > Tops"):
            raise AssertionError

    def verify_first_product_price_label(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\first_product_price_label.png")
        self.log.info(self.get_first_product_price_label().text+' is visible')
        assert self.get_first_product_price_label().text == "Rs. 500"
        if not (self.get_first_product_price_label().text == "Rs. 500"):
            raise AssertionError

    def verify_first_product_availability_label(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\first_product_availability_label.png")
        self.log.info(self.get_first_product_availability_label().text+' is visible')
        assert self.get_first_product_availability_label().text == "Availability:"
        if not (self.get_first_product_availability_label().text == "Availability:"):
            raise AssertionError

    def verify_first_product_condition_label(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\first_product_condition_label.png")
        self.log.info(self.get_first_product_condition_label().text+' is visible')
        assert self.get_first_product_condition_label().text == "Condition:"
        if not (self.get_first_product_condition_label().text == "Condition:"):
            raise AssertionError

    def verify_first_product_brand_label(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\first_product_brand_label.png")
        self.log.info(self.get_first_product_brand_label().text+' is visible')
        assert self.get_first_product_brand_label().text == "Brand:"
        if not (self.get_first_product_brand_label().text == "Brand:"):
            raise AssertionError

    def verify_tops_product_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\tops_product_banner.png")
        self.log.info(self.get_tops_product_banner().text+' is visible')
        assert self.get_tops_product_banner().text == "WOMEN - TOPS PRODUCTS"
        if not (self.get_tops_product_banner().text == "WOMEN - TOPS PRODUCTS"):
            raise AssertionError

    def verify_tshirt_product_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\tshirt_product_banner.png")
        self.log.info(self.get_tshirt_product_banner().text+' is visible')
        assert self.get_tshirt_product_banner().text == "MEN - TSHIRTS PRODUCTS"
        if not (self.get_tshirt_product_banner().text == "MEN - TSHIRTS PRODUCTS"):
            raise AssertionError

    def verify_polo_brand_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\polo_brand_banner.png")
        self.log.info(self.get_polo_brand_banner().text+' is visible')
        assert self.get_polo_brand_banner().text == "BRAND - POLO PRODUCTS"
        if not (self.get_polo_brand_banner().text == "BRAND - POLO PRODUCTS"):
            raise AssertionError

    def verify_h_and_m_brand_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\H&M_brand_banner.png")
        self.log.info(self.get_h_and_m_brand_banner().text+' is visible')
        assert self.get_h_and_m_brand_banner().text == "BRAND - H&M PRODUCTS"
        if not (self.get_h_and_m_brand_banner().text == "BRAND - H&M PRODUCTS"):
            raise AssertionError

    def input_search_product(self, search_keyword):
        self.get_search_product().send_keys(search_keyword)

    def input_search_product_btn(self):
        self.get_search_product_btn().click()

    def search_product_input(self, search_keyword):
        self.input_search_product(search_keyword)
        self.input_search_product_btn()

    def scroll_and_click_add_to_cart_btn(self):
        addToCartBtn = self.get_add_to_cart_btn()
        self.driver.execute_script("arguments[0].scrollIntoView();", addToCartBtn)
        addToCartBtn.click()

    def click_continue_shopping_btn(self):
        self.get_continue_shopping_btn().click()

    def click_add_to_cart2_btn(self):
        self.get_add_to_cart2_btn().click()

    def input_product_qty(self):
        time.sleep(2)
        self.get_product_qty().click()
        self.get_product_qty().clear()
        self.get_product_qty().send_keys("4")

    def click_view_product_add_to_cart_btn(self):
        self.get_view_product_add_to_cart_btn().click()

    def click_view_cart_btn(self):
        self.get_view_cart_link().click()

    def search_view_product_add_to_cart(self):
        self.click_view_product_add_to_cart_btn()
        self.click_view_cart_btn()

    def click_tops_category(self):
        self.get_tops_category().click()

    def click_men_category(self):
        self.get_men_category().click()

    def click_tshirt_category(self):
        self.get_tshirt_category().click()

    def verify_brands(self):
        self.log.info(self.get_brands().is_displayed())

    def click_polo_brand(self):
        polo_brand = self.get_polo_brand()
        self.driver.execute_script("arguments[0].scrollIntoView();", polo_brand)
        polo_brand.click()

    def click_h_and_m_brand(self):
        handm_brand = self.get_h_and_m_brand()
        self.driver.execute_script("arguments[0].scrollIntoView();", handm_brand)
        handm_brand.click()

    def click_men_tshirt(self):
        men_tshirt = self.get_men_tshirt()
        self.driver.execute_script("arguments[0].scrollIntoView();", men_tshirt)
        men_tshirt.click()

    def click_view_product_btn(self):
        view_product = self.get_view_product_btn()
        self.driver.execute_script("arguments[0].scrollIntoView();", view_product)
        view_product.click()

    def input_review_name(self, rev_name):
        review_name = self.get_review_name()
        self.driver.execute_script("arguments[0].scrollIntoView();", review_name)
        review_name.send_keys(rev_name)

    def input_review_email(self, rev_email):
        review_email = self.get_review_email()
        self.driver.execute_script("arguments[0].scrollIntoView();", review_email)
        review_email.send_keys(rev_email)

    def input_review_input(self, rev_input):
        review_input = self.get_review_input()
        self.driver.execute_script("arguments[0].scrollIntoView();", review_input)
        review_input.send_keys(rev_input)

    def click_review_submit_btn(self):
        review_submit = self.get_review_submit_btn()
        self.driver.execute_script("arguments[0].scrollIntoView();", review_submit)
        review_submit.click()

    def search_review(self, rev_name, rev_email, rev_input):
        self.input_review_name(rev_name)
        self.input_review_email(rev_email)
        self.input_review_input(rev_input)
        self.click_review_submit_btn()
