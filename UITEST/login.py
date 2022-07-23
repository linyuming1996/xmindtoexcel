import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element(By.ID,'kw').send_keys('iphone')
driver.find_element(By.ID,'su').click()
driver.maximize_window()
time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# element = WebDriverWait(driver,10,1).until(lambda x: x)
# select = Select(driver.find_element_by_id())
# select.select_by_index()
# alert = driver.switch_to.alert
# alert.text
js = "window.scrollTo(0,500)"
driver.execute_script(js)
# alert.accept()
# alert.dismiss()
time.sleep(5)
pngpath = "./png/{}.jpg".format(time.strftime("%Y%m%d%H%M"))
print(pngpath)
driver.get_screenshot_as_file(pngpath)
driver.close()
driver.quit()