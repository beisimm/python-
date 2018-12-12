from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
"""
QQ空间批量点赞,
注意配置相应版本的chromedriver到当前目录下,
作者:鹿财 QQ:345199390
有什么私活的请联系我
"""

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Mobile Safari/537.36')

browser = webdriver.Chrome('./chromedriver', options=options)
browser.get('https://qzone.qq.com/')
# 等待
browser.implicitly_wait(5)
# 输入qq号
browser.find_element_by_id('u').send_keys('495212365')
# 输入qq密码
browser.find_element_by_id('p').send_keys('a456123.')
browser.find_element_by_id('go').click()
# 等待10秒手动解决验证码
time.sleep(10)

while True:
    try:
        like = browser.find_element_by_xpath('//button[text()="赞"]')
        top = int(like.location["y"])
        browser.execute_script('document.documentElement.scrollTop={}'.format(top))
        ActionChains(browser).move_to_element(like).click().perform()



    except Exception as e:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        load_most = browser.find_element_by_xpath('//button[text()="加载更多"]')
        print(load_most)
        ActionChains(browser).move_to_element(load_most).click().perform()
