import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchScreen:
    lst_way_xpath = "//*[@class='flight-form max-container-width']//span/span"
    txt_from_xpath = "(//input[@class='c-input u-v-align-middle'])[1]"
    drp_fromLocs_xpath = "//*[@class='airport']"
    wait_xpath = "(//*[@class='autocompleter-scroll-cntr'])[1]"
    txt_to_xpath = "(//*[@class='c-input u-v-align-middle'])[2]"
    drp_toLocs_xpath = "//*[contains(@class,'result-row flight-airport u-box-result')]"
    lst_departDate_xpath = "//*[@class='rd-days-body']//td[not(contains(@class,'rd-day-disabled')) and not(contains(" \
                           "@class,'rd-day-concealed'))] "
    lst_returnDate_xpath = "(//*[@class='rd-date'])[2]//table/tbody//td[not(contains(@class,'trip-date end-of-month')) and not(contains(@class,'rd-day-concealed'))]"
    btn_nextArrow_xpath = "(//*[@class='ixi-icon-arrow rd-next'])[2]"
    btn_search_xpath = "(//*[@class='u-ripple'])[1]"
    home_fromLoc_xpath = "(//*[@class='c-input u-v-align-middle'])[1]"
    home_toLoc_xpath = "(//*[@class='c-input u-v-align-middle'])[2]"
    cb_stop_xpath = "(//*[@class='checkbox-list-item ']/span)[3]"
    rb_fromFlight_xpath = "(//*[@class='result-col-inner'])[1]/div[1]/div/div/div"
    text_fromFlight_xpath = "(//*[@class='c-flight-listing-split-row selected hide-detail'])[1]/div/div[3]/div"
    rb_toFlight_xpath = "(//*[@class='result-col-inner'])[2]/div[1]/div/div/div"
    btn_book_xpath = "(//button[@class='c-btn u-link enabled'])[last()]"
    btn_loginToProceed_xpath = "//button[text()='login to proceed']"
    popup_login_xpath = "//*[@class='main-interface']/div[2]"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_roundTrip(self, type_input):
        # time.sleep(2)
        lst = self.driver.find_elements_by_xpath(self.lst_way_xpath)
        for way in lst:
            if way.text == type_input:
                way.click()
                break
            else:
                pass

    def select_from_loc(self, fromLoc_input):
        self.driver.find_element_by_xpath(self.txt_from_xpath).click()
        self.driver.find_element_by_xpath(self.txt_from_xpath).send_keys(fromLoc_input)
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.drp_fromLocs_xpath)))
        fromLocs = self.driver.find_elements_by_xpath(self.drp_fromLocs_xpath)
        for loc in fromLocs:
            location_name = loc.text
            if location_name == fromLoc_input:
                loc.click()
                break
            else:
                pass

    def select_to_loc(self, toLoc_input):
        self.driver.find_element_by_xpath(self.txt_to_xpath).send_keys(toLoc_input)
        time.sleep(2)
        dest_locations = self.driver.find_elements_by_xpath(self.drp_fromLocs_xpath)
        for dest_loc in dest_locations:
            if dest_loc.text == toLoc_input:
                dest_loc.click()
                break
            else:
                pass

    def select_depart_date(self, departDate_input):
        lst_dates = self.driver.find_elements_by_xpath(self.lst_departDate_xpath)
        for date in lst_dates:
            actual_date = date.get_attribute("data-date")
            if actual_date == departDate_input:
                date.click()
                break
            else:
                pass

    def select_return_date(self, returnDate_input):
        time.sleep(2)
        lst_returnDates = self.driver.find_elements_by_xpath(self.lst_returnDate_xpath)
        for returnDate in lst_returnDates:
            actual_date = returnDate.get_attribute("data-date")
            if actual_date == returnDate_input:
                returnDate.click()
                break
            else:
                pass

    def click_search_btn(self):
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()

    def verify_inputs(self, fromLoc_input, toLoc_input):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains(fromLoc_input))
        from_loc = self.driver.find_element_by_xpath(self.home_fromLoc_xpath)
        actual_fromLoc = from_loc.get_attribute("value")
        #Validating whether FROM location entered in search screen matches with the Home screen
        if fromLoc_input in actual_fromLoc:
            assert True
        else:
            assert False
        # Validating whether TO location entered in search screen matches with the Home screen
        to_loc = self.driver.find_element_by_xpath(self.home_toLoc_xpath)
        actual_toLoc = to_loc.get_attribute("value")
        if toLoc_input in actual_toLoc:
            assert True
        else:
            assert False

    def select_oneStop(self):
        self.driver.find_element_by_xpath(self.cb_stop_xpath).click()

    def select_flights(self):
        #Select the 1st flight two ways
        rb_fromFlight = self.driver.find_element_by_xpath(self.rb_fromFlight_xpath)
        if rb_fromFlight.is_selected:
            assert True
        else:
            self.driver.find_element_by_xpath(self.rb_fromFlight_xpath).click()
        rb_toFlight = self.driver.find_element_by_xpath(self.rb_toFlight_xpath)
        if rb_toFlight.is_selected:
            assert True
        else:
            self.driver.find_element_by_xpath(self.rb_toFlight_xpath).click()
        #Fetch the text such as Airline name, flight number, total payable

        #Click Book button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_book_xpath)))
        self.driver.find_element_by_xpath(self.btn_book_xpath).click()

        #Click Login to Proceed button
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_loginToProceed_xpath)))
        self.driver.find_element_by_xpath(self.btn_loginToProceed_xpath).click()

        #Verify the login pop-up
        time.sleep(2)
        popup_text = self.driver.find_element_by_xpath(self.popup_login_xpath).text
        if popup_text == 'Log in to ixigo':
            assert True
        else:
            assert False






















