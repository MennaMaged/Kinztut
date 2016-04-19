import unittest
from selenium import webdriver

class TestCase1(unittest.TestCase):
    @classmethod
    def setUp(cls):

        fp = webdriver.FirefoxProfile('C:/Profiles')
        cls.driver = webdriver.Firefox(fp)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://www.kinztut.com/")

    def test_signIn(self):

        signIn_btn = self.driver.find_element_by_xpath(".//*[@id='home']/div[4]/div[1]/div[2]/div/div/div[2]/ul/li[6]/div/a[1]")
        signIn_btn.click()
        signIn_title = self.driver.find_element_by_xpath(".//*[@id='sl-dialog-login']/div/div/div[1]/div").text
        self.driver.implicitly_wait(30)
        self.assertEqual(signIn_title,'Sign In')
        self.driver.implicitly_wait(30)
        email_txt = self.driver.find_element_by_xpath(".//*[@id='customer_login']/input[1]")
        email_txt.clear()
        email_txt.send_keys("Kmonir@integrant.com")
        pass_txt = self.driver.find_element_by_xpath(".//*[@id='customer_login']/input[2]")
        pass_txt.clear()
        pass_txt.send_keys("hello_1234")
        submit_btn = self.driver.find_element_by_xpath(".//*[@id='customer_login']/input[3]")
        submit_btn.click()
        self.driver.implicitly_wait(30)
        title_lbl = self.driver.find_element_by_xpath(".//*[@id='LayoutColumn2']/div/div/h1")
        self.assertTrue(title_lbl.is_displayed())

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()