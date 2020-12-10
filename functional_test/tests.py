from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time
import unittest
#make sure website and server are working
#big picture testing

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        #set headless
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.headless = True

        self.browser = webdriver.Chrome(executable_path='C:/Users/zhang/OneDrive/PTC/User Testing/Week 3 Selenium/Selenium/chromedriver_win32/chromedriver.exe', options=ChromeOptions)
        self.browser.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.browser.quit()

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

    #@unittest.SkipTest #ignore a test
    @unittest.SkipTest
    def test_title(self):
        self.assertIn('Django', self.browser.title, 'Wrong Title')

    
    def test_can_start_a_list_and_retrieve_it_later(self):

        #She notices the page title and header mention to-do lists
        self.browser.get(self.live_server_url)
        
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
        )

        #She types "Buy peacock feathers" into a text box(Edith's hobby is trying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        #when she hits enter, the page updates, and now the page lists
        #"1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some 
        #explanatory text to that effect
        self.fail('Finish the test!')

        #She visits the URL - her to-do list is still there

        #Satisfied, she goes back to sleep

