"""
汽车之家二级页面爬取
1. 提取汽车详情页链接 <a href="/dealer/二级页面链接"
2. 二级页面提取数据
3. 换页爬取
"""

import requests as req
import re
import random
import time


class Che168Spider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/baoma/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; '
                                      '.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; '
                                      '.NET4.0C; CIBA; Maxthon 2.0)'}
        self.regex_sophomore_link = '<a href="/dealer/(.*?)"'

    def func_get_html(self, url):
        """
        获取响应内容
        :param url:
        :return:
        """
        html = req.get(url=url, headers=self.headers).content.decode('gb2312')
        return html

    def func_regex_interpreted(self, html, regex):
        """
        解析正则表达式
        :param html:
        :param regex:
        :return:
        """
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        return r_list
