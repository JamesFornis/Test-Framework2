import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.utils import Utils


class AccntInfo(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ACCNTINFO_VISIBLE = "//b[normalize-space()='Enter Account Information']"
    GENDER = "//div[@id='uniform-id_gender1']"
    PASSWORD = "//input[@id='password']"
    DAY = "//select[@id='days']"
    MONTH = "//select[@id='months']"
    YEAR = "//select[@id='years']"
    NEWSLETTER_CHK = "//input[@id='newsletter']"
    PARTNER_CHK = "//input[@id='optin']"
    FIRST_NAME = "//input[@id='first_name']"
    LAST_NAME = "//input[@id='last_name']"
    COMPANY = "//input[@id='company']"
    ADDRESS1 = "//input[@id='address1']"
    ADDRESS2 = "//input[@id='address2']"
    COUNTRY = "//select[@id='country']"
    STATE = "//input[@id='state']"
    CITY = "//input[@id='city']"
    ZIPCODE = "//input[@id='zipcode']"
    MOBILE = "//input[@id='mobile_number']"
    CREATE_ACCOUNT_BTN = "//button[normalize-space()='Create Account']"
    COUNTRY_NAME = "//ul[@id='address_delivery']//li[@class='address_country_name'][normalize-space()='Canada']"
    MOBILE_NUMBER = "(//li[@class='address_phone'][normalize-space()='09235873765'])[1]"
    ADDRESS = "(//li[@class='address_address1 address_address2'][normalize-space()='Cebu City'])[1]"
    COMPANY_DETAIL = "(//li[@class='address_address1 address_address2'][normalize-space()='Cheq Systems Inc'])[1]"
    STATE_CITY_ZIP = "(//li[@class='address_city address_state_name address_postcode'][contains(text(),'Cebu Cebu')])[1]"
    GENDER_FNAME_LNAME = "(//li[@class='address_firstname address_lastname'][normalize-space()='Mr. James Fornis'])[1]"
    GENDER_FNAME_LNAME_BILLING = "(//li[@class='address_firstname address_lastname'][normalize-space()='Mr. James Fornis'])[2]"
    COMPANY_DETAIL_BILLING = "(//li[@class='address_address1 address_address2'][normalize-space()='Cheq Systems Inc'])[2]"
    ADDRESS_BILLING = "(//li[@class='address_address1 address_address2'][normalize-space()='Cebu City'])[4]"
    STATE_CITY_ZIP_BILLING = "(//li[@class='address_city address_state_name address_postcode'][contains(text(),'Cebu Cebu')])[2]"
    COUNTRY_NAME_BILLING = "(//li[@class='address_country_name'][normalize-space()='Canada'])[2]"
    MOBILE_NUMBER_BILLING = "(//li[@class='address_phone'][normalize-space()='09235873765'])[2]"

    def get_account_info_banner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.ACCNTINFO_VISIBLE)

    def get_gender_fname_lname(self):
        return self.driver.find_element(By.XPATH, self.GENDER_FNAME_LNAME)

    def get_gender_fname_lname_billing(self):
        return self.driver.find_element(By.XPATH, self.GENDER_FNAME_LNAME_BILLING)

    def get_company_detail_billing(self):
        return self.driver.find_element(By.XPATH, self.COMPANY_DETAIL_BILLING)

    def get_address_billing(self):
        return self.driver.find_element(By.XPATH, self.ADDRESS_BILLING)

    def get_country_name_billing(self):
        return self.driver.find_element(By.XPATH, self.COUNTRY_NAME_BILLING)

    def get_city_state_zip_billing(self):
        return self.driver.find_element(By.XPATH, self.STATE_CITY_ZIP_BILLING)

    def get_mobile_number_billing(self):
        return self.driver.find_element(By.XPATH, self.MOBILE_NUMBER_BILLING)

    def get_gender(self):
        return self.driver.find_element(By.XPATH, self.GENDER)

    def get_city_state_zip(self):
        return self.driver.find_element(By.XPATH, self.STATE_CITY_ZIP)

    def get_company_detail(self):
        return self.driver.find_element(By.XPATH, self.COMPANY_DETAIL)

    def get_address(self):
        return self.driver.find_element(By.XPATH, self.ADDRESS)

    def get_mobile_number(self):
        return self.driver.find_element(By.XPATH, self.MOBILE_NUMBER)

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.PASSWORD)

    def get_day(self):
        return Select(self.driver.find_element(By.XPATH, self.DAY))

    def get_month(self):
        return Select(self.driver.find_element(By.XPATH, self.MONTH))

    def get_year(self):
        return Select(self.driver.find_element(By.XPATH, self.YEAR))

    def get_newsletter(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.NEWSLETTER_CHK)

    def get_partner(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.PARTNER_CHK)

    def get_first_name(self):
        return self.driver.find_element(By.XPATH, self.FIRST_NAME)

    def get_last_name(self):
        return self.driver.find_element(By.XPATH, self.LAST_NAME)

    def get_company(self):
        return self.driver.find_element(By.XPATH, self.COMPANY)

    def get_address1(self):
        return self.driver.find_element(By.XPATH, self.ADDRESS1)

    def get_address2(self):
        return self.driver.find_element(By.XPATH, self.ADDRESS2)

    def get_country(self):
        return Select(self.driver.find_element(By.XPATH, self.COUNTRY))

    def get_state(self):
        return self.driver.find_element(By.XPATH, self.STATE)

    def get_city(self):
        return self.driver.find_element(By.XPATH, self.CITY)

    def get_zipcode(self):
        return self.driver.find_element(By.XPATH, self.ZIPCODE)

    def get_mobile(self):
        return self.driver.find_element(By.XPATH, self.MOBILE)

    def get_create_accnt_btn(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.CREATE_ACCOUNT_BTN)

    def get_delivery_country_name(self):
        return self.driver.find_element(By.XPATH, self.COUNTRY_NAME)

    def verify_account_info_banner(self):
        self.driver.save_screenshot("C:\\Users\\James Fornis\\PycharmProjects\\TestFramework\\screenshots\\account_information_banner.png")
        self.log.info(self.get_account_info_banner().text+' is visible')
        assert self.get_account_info_banner().text == "ENTER ACCOUNT INFORMATION"
        if not (self.get_account_info_banner().text == "ENTER ACCOUNT INFORMATION"):
            raise AssertionError

    def click_gender(self):
        self.get_gender().click()

    def enter_password(self, password):
        self.get_password().send_keys(password)

    def enter_day(self, dayinfo):
        self.get_day().select_by_visible_text(dayinfo)

    def enter_month(self, monthinfo):
        self.get_month().select_by_visible_text(monthinfo)

    def enter_year(self, yearinfo):
        self.get_year().select_by_visible_text(yearinfo)

    def click_newsletter(self):
        newsletter = self.get_newsletter()
        self.driver.execute_script("arguments[0].scrollIntoView();", newsletter)
        newsletter.click()

    def click_partner(self):
        partner = self.get_partner()
        self.driver.execute_script("arguments[0].scrollIntoView();", partner)
        partner.click()

    def enter_first_name(self, fnames):
        self.get_first_name().send_keys(fnames)

    def enter_last_name(self, lnames):
        self.get_last_name().send_keys(lnames)

    def enter_company(self, compdet):
        self.get_company().send_keys(compdet)

    def enter_address1(self, address1):
        self.get_address1().send_keys(address1)

    def enter_address2(self, address2):
        self.get_address2().send_keys(address2)

    def enter_country(self, countryname):
        self.get_country().select_by_visible_text(countryname)

    def enter_state(self, state):
        self.get_state().send_keys(state)

    def enter_city(self, city):
        self.get_city().send_keys(city)

    def enter_zipcode(self, zipcode):
        self.get_zipcode().send_keys(zipcode)

    def enter_mobile(self, mobilenum):
        self.get_mobile().send_keys(mobilenum)

    def click_create_accnt_btn(self):
        create_btn = self.get_create_accnt_btn()
        self.driver.execute_script("arguments[0].scrollIntoView();", create_btn)
        create_btn.click()

    def search_accnt_info1(self, password, dayinfo, monthinfo, yearinfo):
        self.enter_password(password)
        self.enter_day(dayinfo)
        self.enter_month(monthinfo)
        self.enter_year(yearinfo)

    def search_accnt_info2(self, fnames, lnames, compdet, address1, address2, countryname, state, city, zipcode, mobilenum):
        self.enter_first_name(fnames)
        self.enter_last_name(lnames)
        self.enter_company(compdet)
        self.enter_address1(address1)
        self.enter_address2(address2)
        self.enter_country(countryname)
        self.enter_state(state)
        self.enter_city(city)
        self.enter_zipcode(zipcode)
        self.enter_mobile(mobilenum)
        self.click_create_accnt_btn()

    def verify_delivery_country_name(self, country_name):
        assert self.get_delivery_country_name().text == country_name
        if not (self.get_delivery_country_name().text == country_name):
            raise AssertionError

    def verify_delivery_country_name_billing(self, country_name):
        assert self.get_country_name_billing().text == country_name
        if not (self.get_country_name_billing().text == country_name):
            raise AssertionError

    def verify_mobile_number(self, mobilenum):
        assert self.get_mobile_number().text == mobilenum
        if not (self.get_mobile_number().text == mobilenum):
            raise AssertionError

    def verify_mobile_number_billing(self, mobilenum):
        assert self.get_mobile_number_billing().text == mobilenum
        if not (self.get_mobile_number_billing().text == mobilenum):
            raise AssertionError

    def verify_address(self, address1):
        assert self.get_address().text == address1
        if not (self.get_address().text == address1):
            raise AssertionError

    def verify_address_billing(self, address1):
        assert self.get_address_billing().text == address1
        if not (self.get_address_billing().text == address1):
            raise AssertionError

    def verify_company_detail(self, compdet):
        assert self.get_company_detail().text == compdet
        if not (self.get_company_detail().text == compdet):
            raise AssertionError

    def verify_company_detail_billing(self, compdet):
        assert self.get_company_detail_billing().text == compdet
        if not (self.get_company_detail_billing().text == compdet):
            raise AssertionError

    def verify_city_state_zip_detail(self, state, city, zipcode):
        assert self.get_city_state_zip().text == state+" "+city+" "+zipcode
        if not (self.get_city_state_zip().text == state+" "+city+" "+zipcode):
            raise AssertionError

    def verify_city_state_zip_detail_billing(self, state, city, zipcode):
        assert self.get_city_state_zip_billing().text == state+" "+city+" "+zipcode
        if not (self.get_city_state_zip_billing().text == state+" "+city+" "+zipcode):
            raise AssertionError

    def verify_gender_fname_lname_detail(self, fnames, lnames):
        assert self.get_gender_fname_lname().text == "Mr. "+fnames+" "+lnames
        if not (self.get_gender_fname_lname().text == "Mr. "+fnames+" "+lnames):
            raise AssertionError

    def verify_gender_fname_lname_detail_billing(self, fnames, lnames):
        assert self.get_gender_fname_lname_billing().text == "Mr. "+fnames+" "+lnames
        if not (self.get_gender_fname_lname_billing().text == "Mr. "+fnames+" "+lnames):
            raise AssertionError

    def verify_address_info(self, fnames, lnames, compdet, address1, state, city, zipcode, country_name, mobilenum):
        self.verify_gender_fname_lname_detail(fnames, lnames)
        self.verify_company_detail(compdet)
        self.verify_address(address1)
        self.verify_city_state_zip_detail(state, city, zipcode)
        self.verify_delivery_country_name(country_name)
        self.verify_mobile_number(mobilenum)

    def verify_address_info_billing(self, fnames, lnames, compdet, address1, state, city, zipcode, country_name, mobilenum):
        self.verify_gender_fname_lname_detail_billing(fnames, lnames)
        self.verify_company_detail_billing(compdet)
        self.verify_address_billing(address1)
        self.verify_city_state_zip_detail_billing(state, city, zipcode)
        self.verify_delivery_country_name_billing(country_name)
        self.verify_mobile_number_billing(mobilenum)
