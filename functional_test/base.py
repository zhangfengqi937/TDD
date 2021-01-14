from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time
import unittest
#make sure website and server are working
#big picture testing

MAX_WAIT = 10
class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        #set headless
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.headless = True

        self.browser = webdriver.Chrome(executable_path='C:/Users/zhang/OneDrive/PTC/User Testing/Week 3 Selenium/Selenium/chromedriver_win32/chromedriver.exe', options=ChromeOptions)
        self.browser.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = self.browser.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def wait_to_be_logged_in(self, email):
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Log out')
        )
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)


    def wait_to_be_logged_out(self, email):
        self.wait_for(
            lambda: self.browser.find_element_by_name('email')
        )
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)