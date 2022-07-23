import requests
#创建session对象
session = requests.Session()
#获取验证码
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
#登录
login_url =  "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
"username": "18078354736",
"password": "123456",
"verify_code": "8888"
}
response = session.post(url=login_url,data=login_data)
print(response.json())
#我的订单
response = session.get("http://localhost/Home/Order/order_list.html")
print(response.text)