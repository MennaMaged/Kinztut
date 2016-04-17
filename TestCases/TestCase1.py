from selenium import webdriver

fp = webdriver.FirefoxProfile('C:/Profiles')
driver = webdriver.Firefox(fp)
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.kinztut.com/")

SignIn_BTN = driver.find_element_by_xpath(".//*[@id='home']/div[4]/div[1]/div[2]/div/div/div[2]/ul/li[6]/div/a[1]")
SignIn_BTN.click()

driver.close()