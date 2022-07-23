import pytest
from pageelements.webpage import BaiduPage
from pageelements.webpage import EmailPage
from common.readconfig import configini
from utils.times import sleep
import allure


@allure.feature('测试场景1')    # 标记测试场景
class Test01:
    @allure.story('测试用例1-1')    # 标记测试用例
    @allure.severity('trivial')    # 标记用例级别
    @pytest.mark.run(order=0)   # 标记用例执行顺序
    def test_search(self, browser):
        """打开百度"""
        self.driver = BaiduPage(browser)
        self.driver.get(configini.url)
        self.driver.searchinput.send_keys(configini.SearchKey)
        self.driver.searchbutton.click()
        sleep(3)
        self.driver.Emaillink.click()
        print('搜索系统')

    @allure.story('测试用例1-2')
    @allure.severity('normal')
    @pytest.mark.run(order=1)
    def test_loginsystem(self, browser):
        """登录系统"""
        self.driver = EmailPage(browser)
        handler = self.driver.window_handles
        self.driver.switch_to_window(handler[-1])
        self.driver.Emailuser.send_keys(configini.emailname)
        self.driver.Emailpassword.send_keys(configini.emailpassword)
        self.driver.Emaillogin.click()
        print('进入系统')
        assert self.driver.get_title == configini.SearchKey


if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py'])
