import re
import time
import random
import requests as req


class MaoyanSpier:
    def __init__(self, data='', top=1):
        self.filename = '猫眼电影TOP100榜单.txt'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.regex = '<div class="movie-item-info">.*?title="(/w+)".*?<p class="star">(/w+)</p>.*?' \
                     '<p class="releasetime">(/w+)</p>'
        self.data = data
        self.top = top

    def get_html(self, url):
        """获得html"""
        html = req.get(url=url, headers=self.headers).content.decode('utf-8')
        return html

    def parse_html(self, html):
        """解析信息"""
        pattern = re.compile(self.regex, re.S)
        r_list01 = pattern.findall(html)
        r_list02 = self.delete_none(r_list01)
        data = self.extract_data(r_list02)
        return data

    def delete_none(self, list):
        for r in list:
            for number in range(0, 3):
                r[number] = r[number].strip()
        return list

    def save_file(self):
        with open(self.filename, mode='w', encoding='utf-8') as f:
            f.write(self.data)
            f.close()

    def extract_data(self, list):
        for r in list:
            title = '电影名称' + r[0] + '\n'
            star = r[1] + '\n'
            release_time = '上映时间' + r[2] + '\n\n'
            self.data += 'TOP:\n' % self.top + title + star + release_time
            self.top += 1
        return self.data

    def delay(self):
        time.sleep(random.random() * 2 + 0.5)

    def run(self):
        for page in (0, 10):
            url = self.url.format(page * 10)
            html = self.get_html(url)
            self.parse_html(html)
            self.save_file()
            self.delay()
            print('已完成第%d页' % (page + 1))

"""
暂时无法得知代码是否可行
"""
if __name__ == '__main__':
    spider = MaoyanSpier()
    spider.run()
