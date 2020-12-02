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

    def test_title(self):
        self.assertIn('Django', self.browser.title, 'Wrong Title')

if __name__ == '__main__':
    #calls the class if it is not instantiated elsewhere
    unittest.main()

