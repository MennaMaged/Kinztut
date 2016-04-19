import unittest
from selenium import webdriver

class TestCase1(unittest.TestCase):
    def setUp(self):

        fp = webdriver.FirefoxProfile('C:/Profiles')
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.kinztut.com/")

    def test_signIn(self):

        signIn_BTN = self.driver.find_element_by_xpath(".//*[@id='home']/div[4]/div[1]/div[2]/div/div/div[2]/ul/li[6]/div/a[1]")
        signIn_BTN.click()
        signIn_title = self.driver.find_element_by_xpath(".//*[@id='sl-dialog-login']/div/div/div[1]/div").text
        self.assertEqual(signIn_title,'Sign In')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()