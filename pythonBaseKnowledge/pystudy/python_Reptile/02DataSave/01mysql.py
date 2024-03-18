import pymysql
from urllib import parse
import requests as req
import re

"""
b站查询内容观看最多的视频
"""


class BilibiliSpider:
    def __init__(self):
        """基本变量"""
        self.url = 'https://search.bilibili.com/all?keyword={}&order=click'
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; '
                                      '.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; '
                                      '.NET4.0C; CIBA; Maxthon 2.0)'}
        self.regex = '</span><a title="(.*?)".*?' \
                     'href="//www.bilibili.com/video/(.*?)\?.*?' \
                     '<div class="des hide">(.*?)</div>.*?' \
                     '<i class="icon-playtime"></i>(.*?)</span>.*?' \
                     '<i class="icon-date"></i>(.*?)</span>.*?' \
                     'class="up-name">(.*?)</a>'
        self.db = pymysql.connect(host='localhost', user='root', password='perseus0709?', db='mydb',
                                  charset='utf8')
        self.cur = self.db.cursor()

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
        self.save_html(r_list01)

    def save_html(self, r_list):
        ins = 'insert into bilimytable values(%s,%s,%s,%s,%s,%s)'
        for r in r_list:
            list_li = []
            for c in range(0, len(r)):
                list_li.append(r[c].strip())
            self.cur.execute(ins, list_li)
            self.db.commit()

    def run(self):
        keyword = input('请输入查询内容:')
        params = parse.quote(keyword)
        url = self.url.format(params)
        html = self.get_html(url)
        self.parse_html(html)
        self.cur.close()
        self.db.close()
        print('抓取完成')


if __name__ == '__main__':
    spider = BilibiliSpider()
    spider.run()
