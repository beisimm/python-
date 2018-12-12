import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

wd = input('输入查询内容: ')

headers = {
    # "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
# "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

req = urllib.request.Request(
    url=url + urllib.parse.quote(wd),
    headers=headers
)
response = urllib.request.urlopen(req)
# print(response.read())

with open('02.html', 'wb')  as f:
   f.write(response.read())