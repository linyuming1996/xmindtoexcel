#导包
import unittest
import time
#from scripts.test02_login2 import TestLoginAPI
from scripts.test01_login_db import TestLoginAPI
from tools.HTMLTestRunner import HTMLTestRunner
#封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLoginAPI))
#指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

#打开文件流
with open(report,"wb") as f:
    #创建HTMLTestRunner执行器：
    runner = HTMLTestRunner(f,title="接口测试报告")
    #执行测试套件
    runner.run(suite)