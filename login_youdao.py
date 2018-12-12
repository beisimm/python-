import requests
import js2py

context = js2py.EvalJs()
url = "https://logindict.youdao.com/login/acc/login"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

username = "beisitmm@163.com"  # 真实账号

password = "a456123."  # 真实密码

with open('logincom.js', 'r') as f:
    context.execute(f.read())
password_encrypt = context.hex_md5(password)

data = {
    "app": "web",
    "tp": "urstoken",
    "cf": "7",
    "fr": "1",
    "ru:http": "//dict.youdao.com/search?q=as&tab=#keyfrom=${keyfrom}",
    "product": "DICT",
    "type": "1",
    "um": "true",
    "username":username ,
    "password":password_encrypt ,
    "savelogin": "1"
}

response = requests.post(url, headers=headers, data=data)

with open("login_youdao.html", "wb") as f:
    f.write(response.content)
