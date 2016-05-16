from selenium.webdriver.common.by import By

class MyAccount():

    title_lbl = (By.XPATH,".//*[@id='LayoutColumn2']/div/div/h1")

    def check_page(self):
        lbl_account = self.driver.find_element(*MyAccount.title_lbl).is_displayed()
        return lbl_account



