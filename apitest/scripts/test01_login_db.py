# 导包
#import json
import requests
import unittest
from api.login import LoginAPI
from parameterized import parameterized
from tools.dbutil import DBUtil
# 构造测试数据
def build_data():
    # json_file = "./data/login.json"
    test_data = []
    sql = "select * from t_login"
    db_data = DBUtil.exe_sql(sql)

    # with open(json_file, encoding="utf-8") as f:
    #     json_data = json.load(f)
    for case_data in db_data:
        username = case_data[2]
        password = case_data[3]
        verify_code = case_data[4]
        status_code = case_data[5]
        content_type = case_data[6]
        status = case_data[7]
        msg = case_data[8]
        test_data.append((username, password, verify_code, status_code,
        content_type, status, msg))
        print("test_data = {}".format((username, password, verify_code,
        status_code, content_type, status, msg)))
    return test_data
# 定义测试类
class TestLoginAPI(unittest.TestCase):
# 前置处理
    def setUp(self):
        self.login_api = LoginAPI()
        self.session = requests.Session()

# 后置处理
    def tearDown(self):
        if self.session:
            self.session.close()
# 定义测试方法
    @parameterized.expand(build_data)
    def test01_login(self, username, password, verify_code, status_code,
    content_type, status, msg):
# 调用验证码接口
        response = self.login_api.get_verify_code(self.session)
        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertIn(content_type, response.headers.get("Content-Type"))
        # 调用登录接口
        response = self.login_api.login(self.session, username, password,
        verify_code)
        print(response.json())
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertIn(msg, response.json().get("msg"))