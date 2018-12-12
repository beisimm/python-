import requests

url = "https://www.baidu.com/img/bd_logo1.png"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url,headers=headers)

content = response.content

with open('logo.png', 'wb') as f:
    f.write(content)