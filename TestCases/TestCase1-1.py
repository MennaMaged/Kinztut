import unittest
from selenium import webdriver

class TestCase1(unittest.TestCase):

    # we use classmethod to open the same instance of firefox for all tests
    @classmethod
    def setUp(cls):
        # This line identifies the firefox profile to prevent the subscription step
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

        # comparing between the popup title and the expected title
        self.assertEqual(signIn_title,'Sign In')

        self.driver.implicitly_wait(30)

        # identify and submit the email
        email_txt = self.driver.find_element_by_xpath(".//*[@id='customer_login']/input[1]")
        email_txt.clear()
        email_txt.send_keys("Kmonir@integrant.com")

        #identify and submit the password
        pass_txt = self.driver.find_element_by_xpath(".//*[@id='customer_login']/input[2]")
        pass_txt.clear()
        pass_txt.send_keys("hello_1234")

        # click on the submit button
        submit_btn = self.driver.find_element_by_xpath(".//*[@id='customer_login']/input[3]")
        submit_btn.click()
        self.driver.implicitly_wait(30)

        # After login we check for a lable in the next page which prove that login is done successfully
        title_lbl = self.driver.find_element_by_xpath(".//*[@id='LayoutColumn2']/div/div/h1")
        self.assertTrue(title_lbl.is_displayed())
        self.driver.implicitly_wait(30)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

