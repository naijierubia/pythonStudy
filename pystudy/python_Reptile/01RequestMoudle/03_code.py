from urllib import parse
import requests as req

wd = {'wd': '中野梓', 'pn': '10'}  # 多个查询参数用多个key_value即可
url_baidu = 'http://baidu.com/s?'
params = parse.urlencode(wd)
url_baidu_astusa = url_baidu + params
"""
拼接url的方式还有占位符
url2 = 'http://baidu.com/s?%s'%params
format方法(推荐，可以随时修改参数)
url3 = 'http://baidu.com/s?{}'.format(params)
"""
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; '
                         '.NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)'}

response = req.get(url=url_baidu_astusa, headers=headers).text
print(url_baidu_astusa)
