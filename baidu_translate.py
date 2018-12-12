from pprint import pprint

import requests
import json

url = "https://fanyi.baidu.com/basetrans"

headers = {
"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
}
query = input('您需要查询的: ')
data = {
    "query":query,
    "from":"en",
    "to":"zh"
}
response = requests.post(url, headers=headers, data=data)

content = json.loads(response.content.decode("utf-8"))

print("翻译结果为: ", content["trans"][0]["dst"])
# pprint(content)