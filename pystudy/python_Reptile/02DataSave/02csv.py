import csv
from urllib import parse
import requests as req
import re
"""
b站查询内容观看最多的视频
"""


class BilibiliSpider:
    def __init__(self):
        """基本变量"""
        self.url = 'https://search.bilibili.com/all?keyword={}'
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; '
                                      '.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; '
                                      '.NET4.0C; CIBA; Maxthon 2.0)'}
        self.regex = '</span><a title="(.*?)".*?' \
                     'href="//www.bilibili.com/video/(.*?)\?.*?' \
                     '<div class="des hide">(.*?)</div>.*?' \
                     '<i class="icon-playtime"></i>(.*?)</span>.*?' \
                     '<i class="icon-date"></i>(.*?)</span>.*?' \
                     'class="up-name">(.*?)</a>'

        self.keyword = ''

        """
        分别为标题、BV号、简介、播放、投稿时间、up
        """

    def get_html(self, url):
        """
        获得响应
        """
        html = req.get(url=url, headers=self.headers).content.decode('utf-8')
        return html

    def parse_html(self, html):
        pattern = re.compile(self.regex, re.S)
        r_list01 = pattern.findall(html)
        # r_list02 = self.delete_none(r_list01) 未知原因无法删除空格
        f = open('%s.csv' % self.keyword, mode='w', newline='', encoding='gb18030') # 后两个数据解决windows下的空行和编码问题
        self.save_html(f, r_list01)
        f.close()

    def save_html(self, f, r_list):
        for r in r_list:
            list_li = []
            for c in range(0, len(r)):
                list_li.append(r[c].strip())
            writer = csv.writer(f)
            writer.writerow(list_li)

    def run(self):
        self.keyword = input('请输入查询内容:')
        params = parse.quote(self.keyword)
        url = self.url.format(params)
        html = self.get_html(url)
        self.parse_html(html)

        print('抓取完成')


if __name__ == '__main__':
    spider = BilibiliSpider()
    spider.run()
