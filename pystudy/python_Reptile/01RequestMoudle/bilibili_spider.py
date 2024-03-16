from urllib import parse
import requests as req
import re

"""
b站查询内容观看最多的视频 已经失效
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

        """
        分别为标题、BV号、简介、播放、投稿时间、up
        """
        self.data = ''

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
        self.extract_data(r_list01)

    # def delete_none(self, data):
    #     for r in data:
    #         r_list = list(r)
    #         for number in range(0, 6):
    #             r_list[number] = r_list[number].strip()
    #     return data

    def save_html(self, filename):
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(self.data)
            f.close()

    def extract_data(self, r_list02):
        for r in r_list02:
            title = '标题:' + ''.join(r[0]) + '\n'
            BV = 'BV号:' + ''.join(r[1]) + '\n'
            introduction = '简介:' + ''.join(r[2]) + '\n'
            play_time = '播放次数:' + ''.join(r[3]) + '\n'
            date = '投稿时间:' + ''.join(r[4]) + '\n'
            up = 'up:' + ''.join(r[5]) + '\n'
            line = '-' * 50
            self.data += '\n' + title + up + BV + play_time + date + introduction + line

    def run(self):
        keyword = input('请输入查询内容:')
        params = parse.quote(keyword)
        url = self.url.format(params)
        html = self.get_html(url)
        self.parse_html(html)
        filename = '%s点击排行.txt' % keyword
        self.save_html(filename)
        print('抓取完成')


if __name__ == '__main__':
    spider = BilibiliSpider()
    spider.run()
