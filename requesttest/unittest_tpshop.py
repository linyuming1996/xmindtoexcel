import requests
import unittest
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

    def test01_success(self):
        #发送验证码请求并断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200, response.status_code)
        self.assertIn('image', response.headers.get('Content-Type'))
        #发送登录请求并断言
        login_dada = {
            "username": "18078354736",
            "password": "123456",
            "verify_code": "8888",
        }
        response = self.session.post(url=self.url_login,data = login_dada)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1,response.json().get('status'))
        self.assertIn('登陆成功', response.json().get('msg'))
