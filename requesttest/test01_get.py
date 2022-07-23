import requests
#发送请求
# response = requests.get('http://www.baidu.com')
# #查看响应结果
# response.encoding = 'utf-8'
# print(response.text)
login_url = "http://ihrm-test.itheima.net/api/sys/login"
login_data = {
"mobile": "13800000002",
"password": "123456"
}
response = requests.post(url=login_url,json=login_data)
print(response.json())
