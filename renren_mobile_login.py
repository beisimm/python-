import requests
import js2py
import json

context = js2py.EvalJs()

session = requests.session()

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
}

response = session.get("http://activity.renren.com/livecell/rKey", headers=headers)

context.n = json.loads(response.content.decode("utf-8"))["data"]

phoneNum = "18616358651"  # 用户名
password = "qwer1234"  # 真实的密码

context.t = {
    "password": password
}

with open('setMaxDigits.js', 'r', encoding='utf8') as f:
    context.execute(f.read())

with open('RSA.js', 'r', encoding='utf8') as f:
    context.execute(f.read())

with open('Barrett.js', 'r', encoding='utf8') as f:
    context.execute(f.read())

js = '''
        t.password = t.password.split("").reverse().join("");
        setMaxDigits(130);
        var o = new RSAKeyPair(n.e,"",n.n);
        r = encryptedString(o, t.password);
        t.password = r;
        t.rKey = n.rkey
'''
context.execute(js)

data = {
    "phoneNum": phoneNum,
    "password": context.t["password"],
    "c1": "-100",
    "rKey": context.t["rKey"]
}

headers["Referer"] = "http://activity.renren.com/livecell/log?c1=-100&c2=&c3=&c4=&from_uid=&isFull=&QRCodeRecharge="

session.post("http://activity.renren.com/livecell/ajax/clog", headers=headers, data=data)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

response = session.get("http://safe.renren.com/security/account", headers=headers)

with  open("renren.html", "wb") as f:
    f.write(response.content)
