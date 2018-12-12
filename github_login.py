import requests

url = "https://github.com/session"
login = "345199390@qq.com"
password = "git456123"

headers = {
    "Cookie": "_octo=GH1.1.2093426362.1535805878; _ga=GA1.2.390633633.1535805893; logged_in=no; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; _gh_sess=STRCMjc1WXhYOFRvSkViWUpOYlZrMkV0YlNudlhqUjdwZlN0dkpWU09HSnZneDBKNVQ1MWF3a3FrWXdkMm1vcFFXN0hrMTh4dDQvNFFvSUZWcjVTQyt4WWZwbVIvRHpVbHBDZkdXSkRXdTFycTdrSC9MeFdMMFVIWkVJVHljclQyNytjOTMvZWdQZEUwdENMcmJBN2tvNVdoc25vL0MvbjBzMlAyQ3U3ZU1mUjk1aWphMUQ4dVhmMjdRR255L3JreTBlZituMVh6UGt2UDFzc0pLNmVFbXpNMFFhdEJDOXdYSlhJbXVzUFlBZE90YVA4VFUwNkViR2wyVkdZaDhXQ0VwN29TbmNMQ1ltSktyM2RKMU1uYU40UXJFNzhMdE1IdmpwcUpIQldocUxTcFZycm9IVkxyMlo3OUd1eVdMUGt4SHIrNlM2TWtVSTFBOCswMTEvWTZqa1dUZm4zbVcrOG9zcDVqSkd5cG1wZ1d3c3lLbm9lY3I4Vzd4UFN4a25kdlpaUTlBNjEwTThSWXhiOXRVV0U1NHVjcG80UnhwWUFwc2RjQmhTTDY3L0tvL1FWb2lKWnNjWlNLV2VmNXBJVFJNUjJTcXRFS1hmL0pDVFJ5OUhZZnc9PS0tNlJxRUltYlZFQUJXeUFKTGtEand6UT09--0e8708322f1e1de086805f9e99340ab3c20a581b",
    "Referer": "https://github.com/login",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}

data = {
    "commit": "Sign in",
    "utf8": "✓",
    "authenticity_token": "wdp0Rrh9NC5tjHYLfcnXggSs2tt4SODnLIfvmxEomxMVbPGfDezksN/R7pJugURJzZ1CBoIldSYM6vASZCXRdw==",
    "login": login,
    "password": password,
}

response = requests.post(url, headers=headers, data=data)

cookies = response.cookies

url = "https://github.com/settings/profile"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}

response = requests.get(url, headers=headers, cookies=cookies)

content = response.content

with open('github_user.html', 'wb') as f:
    f.write(content)
