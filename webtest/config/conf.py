import os
import datetime
import time
from selenium.webdriver.common.by import By
class ConfigManager():
    #项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR1 = os.path.dirname(__file__)获取文件所在目录的完整路径：os.path.dirname(__file__)
#BASE_DIR2 = os.path.abspath(__file__)os.path.abspath(__file__)返回的是.py文件的绝对路径
    #页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR,'page_elemnet')
    #报告文件
    REPORT_FILE = os.path.join(BASE_DIR,'Report.html')
    #元素定位的类型
    LOCAL_MODE = {
        'css':By.CSS_SELECTOR,
        'xpath':By.XPATH,
        'name':By.NAME,
        'id':By.ID,
        'class':By.CLASS_NAME,
        'link':By.LINK_TEXT,
        'plink':By.PARTIAL_LINK_TEXT
    }
    #邮箱信息
    ''''''
    EMAIL_INFO={
        'address':''
    }
    #收件人

    ''''''
    @property
    def log_file(self):
        log_dir = os.path.join(self.BASE_DIR,'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir,'{}.log'.format(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
    @property
    def inf_file(self):
        ini_file = os.path.join(self.BASE_DIR,'config','config.ini')
        if not os.path.exists(ini_file):
            #raise FileNotFoundError("配置文件{}不存在".format(ini_file))
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file

conf = ConfigManager()
if __name__ =='__main__':
    print(conf.inf_file)
