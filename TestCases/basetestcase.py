import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        fp = webdriver.FirefoxProfile('C:/Profiles')
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.kinztut.com/")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
