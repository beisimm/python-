import requests
import re
url = 'http://wthrcdn.etouch.cn/WeatherApi'
# params = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
#     "Referer":"http://www.weather.com.cn/"
# }
kv = {
    "city": "深圳"  # 这里传入具体地点即可获得天气信息, 如果没有该地点返回结果为[]
}
html = requests.get(url, params=kv)
content = html.content.decode('utf-8')
dict = {}
city = re.findall('<city>(.*)</city>', content)[0]
dict['地点'] = city
temperature = re.findall('<wendu>(.*)</wendu>', content)[0]
dict['温度'] = temperature
print(dict)


