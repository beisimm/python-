import requests

url = "https://www.baidu.com/s"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

wd = input('请输入查询内容: ')
params = {
    'wd': wd
}

response = requests.get(url,headers=headers, params=params)

content = response.content

with open('requests2.html', 'wb') as f:
    f.write(content)