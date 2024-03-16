"""
确认程序的请求是什么
"""
import requests

url = 'http://httpbin.org/get'
html = requests.get(url=url).text
f = open('headers.txt', mode='w')
f.write(html)
f.close()  # 结果User-Agent直接为re版本

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; '
                         '.NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)'}
html02 = requests.get(url=url, headers=headers).text
g = open('headers_packing.txt', mode='w')
g.write(html02)
g.close()
