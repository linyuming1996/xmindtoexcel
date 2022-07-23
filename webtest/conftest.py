# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from common.readconfig import configini

drivertype = configini.drivertype
driver = None
@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    global DiverType
    if drivertype == 'Chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
    elif drivertype == 'Firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif drivertype == 'ChromeOptions':
        Chromeoptions = webdriver.ChromeOptions()
        Chromeoptions.headless = True
        driver = webdriver.Chrome(options=Chromeoptions)
    return driver
def quitbrowser():
    driver = browser()
    driver.quit()
if __name__ == '__main__':
    print(browser)

