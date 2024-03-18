import requests
import curlify

url = "http://172.16.2.100:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=172.16.2.100&iTermType=1" \
      "&wlanuserip=10.32.52.107&wlanacip=null&wlanacname=null&mac=00-00-00-00-00-00&ip=10.32.52.107&enAdvert=0" \
      "&queryACIP=0&loginMethod=1 "

header = {
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding: gzip, deflate",
    "Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control: max-age=0",
    "Connection: keep-alive",
    "Content-Length: 168",
    "Content-Type: application/x-www-form-urlencoded",
    "Cookie: program=test; vlan=0; ip=10.32.145.221; ssid=null; areaID=null; ISP_select=@cmcc; md5_login2=%2C0%2C2020021006000423@cmcc%7C222211; PHPSESSID=fnt222qsrg24ol2341rsghds51",
    "Host: 172.16.2.100:801",
    "Origin: http://172.16.2.100",
    "Referer: http://172.16.2.100/",
    "Upgrade-Insecure-Requests: 1",
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

data = {
    "DDDDD: ,0,2020021006000423@cmcc",
    "upass: 222211"
}
response = requests.post(url, data, headers=header)
ret = curlify.to_curl(response.request, compressed=True)
with open("login.sh", "w") as f:
    f.write(ret)
print(ret)
response.encoding = "utf8"
print(response.text)
