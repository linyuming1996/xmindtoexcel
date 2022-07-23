from time import sleep
from selenium import webdriver
from logtest import log
import main
wnm = webdriver.Chrome()
wnmlog = log()
wnm.get('https://ipsapro.isoftstone.com/Portal')#登录网址
wnm.maximize_window()#窗口最大化
wnm.implicitly_wait(20)#隐式等待
wnm.find_element_by_xpath('//*[@id="emp_DomainName"]').send_keys(main.myusername)
wnm.find_element_by_id('emp_Password').send_keys(main.mypassword)
wnm.find_element_by_id('BtnLogin').click()
wnm.find_element_by_xpath("//a[@title='我的邮件']").click()
wnm.switch_to.window(wnm.window_handles[-1])
wnm.find_element_by_xpath('//*[@id="account"]').send_keys(main.myusername)
wnm.find_element_by_xpath('//*[@id="password"]').send_keys(main.mypassword)
wnm.find_element_by_xpath('//*[@id="bLogin"]').click()
wnm.find_element_by_xpath('//*[@id="zi_search_inputfield"]').send_keys(main.search)
wnm.find_element_by_class_name('ImgSearch2').click()
sleep(10)
wnmlog.info('程序運行OK')
wnm.quit()

