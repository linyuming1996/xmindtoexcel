"""被测试系统的接口封装"""
import requests
import unittest

#定义接口类
class LoginAPI:
    #初始化
    def __init__(self):
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"

    #获取验证码接口
    def get_verify_code(self,session):
        return session.get(self.url_verify)

    #登陆接口
    def login(self,session,username,password,verify_code):
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        return session.post(url=self.url_login,data=login_data)
