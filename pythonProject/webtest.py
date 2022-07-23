from selenium import webdriver
from time import sleep
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.headless = True
driver = webdriver.Chrome(options=ChromeOptions)
driver.get('https://ipsapro.isoftstone.com/Portal')
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="emp_DomainName"]').send_keys('ymlinf')
driver.find_element_by_xpath('//*[@id="emp_Password"]').send_keys('mingMING@1996')
driver.find_element_by_xpath('//*[@id="BtnLogin"]').click()
sleep(2)
print(driver.title)
print(driver.current_url)

driver.quit()