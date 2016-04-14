import unittest

from selenium import webdriver
from Pages.HomePage import FirstPage

class Base(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.kinztut.com/subscribe.php")

    FirstPage.SignIn()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


