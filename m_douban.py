from pprint import pprint

import requests
import json
import jsonpath
url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
"Referer":"https://m.douban.com/tv/american"
}
for start in range(0,1000, 18):
    params = {
        "os": "ios",
        "for_mobile": "1",
        "callback": "jsonp4",
        "start": start,
        "count": "18",
        "loc_id": "108288",
        "_": "1539333770863"
    }

    response = requests.get(url, headers=headers, params=params)
    content = response.content.decode()
    content = content[8:-2]  # 调整获取的数据
    # pprint(json.loads(content))
    result = json.loads(content)
    title = jsonpath.jsonpath(result,'$..title')
    value = jsonpath.jsonpath(result,'$..value')
    for title, value in zip(title, value):
        print(title, value)
