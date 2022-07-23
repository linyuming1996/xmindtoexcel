import requests
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response.cookies)
PHPSESSID = response.cookies.get('PHPSESSID')
print(PHPSESSID)
login_url =  "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
"username": "18078354736",
"password": "123456",
"verify_code": "8888"
}
cookie = {
    "PHPSESSID": PHPSESSID
}
response = requests.post(url=login_url,data=login_data,cookies=cookie)
print(response.json())
#我的订单
response = requests.get("http://localhost/Home/Order/order_list.html",cookies=cookie)
print(response.text)