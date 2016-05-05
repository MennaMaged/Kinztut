import unittest
from Base.BaseTestCase import BasePage
from Page_Objects.HomePage import HomePage
from Page_Objects.LoginPage import LoginPage
from Page_Objects.MyAccount import MyAccount
from ddt import ddt,data,unpack
from DataSource.LoginDataPage import LoginDataClass

@ddt
class TestCase1(BasePage):

    @data(*LoginDataClass.get_data_from_excel('C:/Users/mmaged/Projects/Kinztut_Automation/Data/LoginData.xlsx', 'Data'))
    @unpack
    def test_signIn(self,email,password):

        HomePage.click_on_sign_button_click(self)
        self.driver.implicitly_wait(30)
        LoginPage.email_submit(self,email)
        LoginPage.password_submit(self,password)
        LoginPage.submit(self)
        self.driver.implicitly_wait(30)

        self.assertTrue(MyAccount.check_page(self))

if __name__ == '__main__':
    unittest.main()

