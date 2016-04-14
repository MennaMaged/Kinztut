import selenium
from selenium.webdriver.common.by import By

class FirstPage():
    SignIn_BTN = (By.LINK_TEXT, 'http://www.kinztut.com/login.php')  # Define Signin Button

    def SignIn(self):
        self.driver.find_element(*FirstPage.SignIn_BTN).click

