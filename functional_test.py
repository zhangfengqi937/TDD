from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
#make sure website and server are working
#big picture testing
class FunctionalTest(unittest.TestCase):
    def setUp(self):
        #set headless
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.headless = True

        self.browser = webdriver.Chrome(executable_path='C:/Users/zhang/OneDrive/PTC/User Testing/Week 3 Selenium/Selenium/chromedriver_win32/chromedriver.exe', options=ChromeOptions)
        self.browser.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.browser.quit()

    #@unittest.SkipTest #ignore a test
    @unittest.SkipTest
    def test_title(self):
        self.assertIn('Django', self.browser.title, 'Wrong Title')

    
    def test_can_start_a_list_and_retrieve_it_later(self):

        #She notices the page title and header mention to-do lists
        self.browser.get('http://127.0.0.1:8000/')
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
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows)
        )

        #There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"

        self.fail('Finish the test!')

        #The page updates again, and now shows both items on her list


if __name__ == '__main__':
    #calls the class if it is not instantiated elsewhere
    unittest.main(warnings = 'ignore')

