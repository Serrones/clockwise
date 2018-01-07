from selenium import webdriver
import unittest



class NewVisitorsTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_access_website_login_register(self):
        # User access website localhost/clockwise
        self.browser.get('http://127.0.0.1:8000')
        # He notices the page title and header mention ClockWise
        self.assertIn('ClockWise', self.browser.title)
        self.fail('Finish the Test!')



if __name__ == '__main__':
    unittest.main()
