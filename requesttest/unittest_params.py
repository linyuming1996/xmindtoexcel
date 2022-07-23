import json
import requests
import unittest
from parameterized import parameterized
#构造测试数据
def buid_data():
    test_data = []
    file = "./data/login.json"
    with open(file,encoding='utf-8') as f:
        json_data = json.load(f)
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            verify_code = case_data.get("verify_code")
            status_code = case_data.get("status_code")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((username,password,verify_code,status_code,status,msg))
    print('test_data='.format(username,password,verify_code,status_code,status,msg))
    return test_data
#创建测试类
class TPShopLogin(unittest.TestCase):
    def setUp(self):
        #实例化session对象
        self.session = requests.Session()
        #定义验证码接口地址
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        #定义登录接口地址
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        #关闭session对象
        self.session.close()

    @parameterized.expand(buid_data())
    def test01_login(self,username,password,verify_code,status_code,status,msg):
        #发送验证码请求并断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200, response.status_code)
        self.assertIn('image', response.headers.get('Content-Type'))
        #发送登录请求并断言
        login_dada = {
            "username": username,
            "password": password,
            "verify_code": verify_code,
        }
        response = self.session.post(url=self.url_login,data = login_dada)
        print(response.json())
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status,response.json().get('status'))
        self.assertIn(msg, response.json().get('msg'))


