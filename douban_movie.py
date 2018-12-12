import requests
import json

url = "https://movie.douban.com/j/search_subjects"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
for page_start in range(0,101,20):
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": "page_start",
    }

    response = requests.get(url, headers=headers, params=params)

    content_json = response.content.decode("utf-8")
    print(content_json)
    content = json.loads(content_json)

    # for movie in content['subjects']:
    #     print(content['subjects'].index(movie), movie['title'], movie['rate'])
