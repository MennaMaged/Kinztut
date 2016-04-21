import unittest
from Base.BaseTestCase import BasePage
from Page_Objects.HomePage import HomePage
from Page_Objects.LoginPage import LoginPage
from Page_Objects.MyAccount import MyAccount

class TestCase1(BasePage):

    def test_signIn(self):

        HomePage.click_on_sign_button_click(self)
        self.driver.implicitly_wait(30)

        LoginPage.email_submit(self)
        LoginPage.password_submit(self)
        LoginPage.submit(self)
        self.driver.implicitly_wait(30)

        self.assertTrue(MyAccount.check_page(self))

if __name__ == '__main__':
    unittest.main()

