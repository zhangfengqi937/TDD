from selenium import webdriver
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

    #She notices the page title and header mention to-do lists
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    #calls the class if it is not instantiated elsewhere
    unittest.main(warnings = 'ignore')

