from selenium.webdriver.common.by import By

class LoginPage():


    email_txt = (By.XPATH,".//*[@id='customer_login']/input[1]")
    pass_txt = (By.XPATH,".//*[@id='customer_login']/input[2]")
    submit_btn = (By.XPATH,".//*[@id='customer_login']/input[3]")

    def email_submit(self,email):
        Login_email = self.driver.find_element(*LoginPage.email_txt).clear()
        Login_email_sendkeys = self.driver.find_element(*LoginPage.email_txt).send_keys(email)

    def password_submit(self,password):
        Login_pass = self.driver.find_element(*LoginPage.pass_txt).clear()
        Login_pass_sendkeys = self.driver.find_element(*LoginPage.pass_txt).send_keys(password)

    def submit(self):
        Login_submit = self.driver.find_element(*LoginPage.submit_btn).click()

