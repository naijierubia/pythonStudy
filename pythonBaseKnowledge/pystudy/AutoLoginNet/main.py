import requests
import socket
import os
import time


class Login:
    def __init__(self):
        self.URL = "http://172.16.2.100:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.16.2.100" \
                   "&iTermType=1&wlanuserip=10.32.111.23&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip=10.32" \
                   ".111.23&enAdvert=0&queryACIP=0&loginMethod=1 "

        self.Headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '168',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': '172.16.2.100:801',
            'Origin': 'http://172.16.2.100',
            'Referer': 'http://172.16.2.100/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/116.0.0.0 Safari/537.36 ',
        }
        self.data = {
            'DDDDD': ',0,2020021006000416@cmcc',
            'upass': '520Ysr1314',
            'R1': '0',
            'R2': '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456',
            'c': 'ACSetting',
            'a': 'Login',
            'protocol': 'http:',
            'hostname': '172.16.2.100',
            'iTermType': '1',
            'wlanuserip': self.get_host_ip(),
            'wlanacip': 'null',
            'wlanacname': 'null',
            'mac': '00 - 00 - 00 - 00 - 00 - 00',
            'ip': self.get_host_ip(),
            'enAdvert': '0',
            'queryACIP': '0',
            'loginMethod': '1',

        }

    @staticmethod
    def get_host_ip():
        ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
        return ip

    @staticmethod
    def net_verify():
        ret = os.system("ping baidu.com -n 1")
        if ret == 0:
            return True
        else:
            return False

    def login_net(self):
        requests.post(self.URL, data=self.data, headers=self.Headers)

    def run(self):
        c = 1
        n = self.net_verify()
        while c <= 5:
            if not n:
                print(time.asctime(), 'No Internet')
                print(time.asctime(), 'try to link [ %d ]...' % c)
                self.login_net()
                time.sleep(3)
                n = self.net_verify()
            else:
                print(time.asctime(), 'Link Successfully')
                break
            c += 1
        else:
            print(time.asctime(), 'Link Failure')

if __name__ == '__main__':
    login = Login()
    login.run()
