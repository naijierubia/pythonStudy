'''
网站后加上robots.txt查看爬虫协议
'''
import requests as req

response = req.get(url='https://www.bilibili.com/')  # get()获取响应对象
f = open('bilibili.txt', mode='w')
html01 = response.text  # 字符串类型
html02 = response.content  # 字节串（图片、视频）
code = req.status_codes  # 获取HTTP响应码
# url = re.url    # 实际数据传输地址
f.write(html01)
f.close()

"""
通过headers中的User-Agent判断是否为正常浏览器
http://httpbin.org/get返回的就是headers文件，下面为正常浏览器请求
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-637a4ca6-44bacb5c485e2c4139744e32"
  }, 
  "origin": "183.217.28.220", 
  "url": "http://httpbin.org/get"
}
"""
