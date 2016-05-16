from selenium.webdriver.common.by import By

class HomePage():

    signIn_btn = (By.XPATH,".//*[@id='home']/div[4]/div[1]/div[2]/div/div/div[2]/ul/li[5]/div/a[1]")


    def click_on_sign_button_click(self):
        signin_click = self.driver.find_element(*HomePage.signIn_btn).click()

