import requests

url = "https://www.baidu.com/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url,headers=headers)

content = response.content

with open('requests1.html', 'wb') as f:
    f.write(content)