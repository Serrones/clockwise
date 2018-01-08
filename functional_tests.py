from selenium import webdriver
import unittest



class NewVisitorsTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_access_website_login_register(self):
        # User access website localhost/tasks
        self.browser.get('http://127.0.0.1:8000/tasks/')
        # He notices the page title and header mention ClockWise
        self.assertIn('ClockWise', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ClockWise', header_text)
        # User notices a NavBar with 3 options, "ABOUT", "LOGIN" and "REGISTER"
        nav_bar = self.browser.find_element_by_tag_name('nav').text
        self.assertIn('ABOUT', nav_bar)
        self.assertIn('LOGIN', nav_bar)
        self.assertIn('REGISTER', nav_bar)



if __name__ == '__main__':
    unittest.main()
