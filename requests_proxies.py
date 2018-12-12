import requests

url = "http://2018.ip138.com/ic.asp"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
proxies = {
    'http':'127.0.0.1:8888'
}

response = requests.get(url, headers=headers, proxies=proxies)

content = response.content

# print(content.decode('utf-8'))
with open('proxies_ip.html', 'wb') as f:
    f.write(content)