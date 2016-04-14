import unittest
from selenium import webdriver
#from Pages.HomePage import FirstPage
#from BaseTestCases.BaseTestCase import Base

class Sign(Base):

    def FirstPageSignIn(self):
        FirstPage.SignIn(self)

if __name__ == '__main__':
    unittest.main()


