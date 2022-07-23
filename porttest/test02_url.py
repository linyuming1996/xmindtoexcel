import requests

response = requests.get('http://baidu.com?q=wnm')
response
print(response.text)
