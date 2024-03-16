from urllib import parse
import requests as req

keyword = input('请输入需要查询的关键字:')
baidu_search = 'https://search.bilibili.com/all?'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; '
                         '.NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; .NET4.0C; CIBA; Maxthon 2.0)'}
filename = '{}.html'.format(keyword)

direct = {'keyword': keyword, '&rder': '=click'}
params = parse.urlencode(direct)
url = baidu_search + params
response = req.get(url=url, headers=headers)
# html = response.text # 转为了text所以乱码 >>> <title>ç¾åº¦å®å¨éªè¯</title>
html = response.content.decode('utf-8')
print('已完成')
with open(filename, mode='w+', encoding='utf-8') as f:
    f.write(html)
    f.close()
"""
如果待编码对象为字符串：
parse.quote()
"""