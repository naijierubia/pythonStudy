from urllib import parse
import requests as req
import time
import random


class BaiduSpider:
    def __init__(self):
        """基本变量"""
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; '
                                      '.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MATP; InfoPath.2; '
                                      '.NET4.0C; CIBA; Maxthon 2.0)'}

    def get_html(self, url):
        """
        获得响应
        """
        html = req.get(url=url, headers=self.headers).content.decode('utf-8')
        return html

    def parse_html(self, html):
        pass

    def save_html(self, html, filename):
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(html)
            f.close()


    def delay(self):
        time.sleep(random.random() * 2 + 0.5)

    def run(self):
        keyword = input('请输入吧名:')
        page_start = int(input('请输入起始页:'))
        page_end = int(input('请输入结束页:'))

        params = parse.quote(keyword)

        for page in range(page_start, page_end + 1):
            pn = (page - 1) * 50
            page_url = self.url.format(params, pn)
            filename = '%s吧_第%d页.html' % (keyword, page)

            html = self.get_html(page_url)
            self.save_html(html, filename)
            print('%s吧_第%d页抓取完成' % (keyword, page))
            self.delay()


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()
