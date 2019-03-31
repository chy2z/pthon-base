"""
演示 requests
"""
import requests

# 下载新浪新闻首页的内容
url = 'http://news.sina.com.cn/china/'
# 用get函数发送GET请求，获取响应
res = requests.get(url)
# 设置响应的编码格式utf-8（默认格式为ISO-8859-1），防止中文出现乱码
res.encoding = 'utf-8'

print(type(res))
print("-------------------------------")
print(res)
print("-------------------------------")
print(res.status_code)  # 状态码200
print("-------------------------------")
# print(res.json())  # 返回json格式
print("-------------------------------")
print(res.headers)  # 头信息
print("-------------------------------")
print(res.encoding)  # 编码方式，一般utf-8
print("-------------------------------")
print(res.text)  # 返回文本

urls='https://car-rental-point.eakay.cn/capi/info'
res = requests.get(urls)
res.encoding = 'utf-8'
print(type(res))
print("-------------------------------")
print(res)
print("-------------------------------")
print(res.status_code)  # 状态码200
print("-------------------------------")
print(res.json())  # 返回json格式
print("-------------------------------")
print(res.headers)  # 头信息
print("-------------------------------")
print(res.encoding)  # 编码方式，一般utf-8
print("-------------------------------")
print(res.text)  # 返回文本

# 一次读取一块，大小为512
for chunk in res.iter_content(chunk_size=512):
    print(chunk)