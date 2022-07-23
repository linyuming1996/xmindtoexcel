import requests

response = requests.get('http://baidu.com')

print('原始的数据编码为：', response.encoding)
response.encoding = 'utf-8'
print('设置后的数据编码为：', response.encoding)
print(response.text)