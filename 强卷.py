import json
import pprint
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')

browser = webdriver.Chrome('./chromedriver', options=options)
browser.get("https://pages.tmall.com/wow/a/act/21024/upr?spm=a211oj.12338607.4488072300.d02.7fb56b1bZHYRPC&wh_weex=true&wh_biz=tm&pos=3&wh_pid=industry-155051&acm=ak-zebra-42992-131720.1003.1.2634748_0&scm=1003.1.ak-zebra-42992-131720.OTHER_1544012700870_2634748&ali_trackid=2:mm_56227121_32534930_150322170:1544621515_245_33848780")
print("打开成功")
cookies = browser.get_cookies()
pprint(cookies[0])
cookies_dict = json.dumps(cookies)
print(cookies_dict)
# qiangjuan = browser.find_element_by_xpath('//div[@class="coupon-area"]/a')
# print("定位成功")
# qiangjuan.click()
# print("点击成功")