from selenium import webdriver
import time
from io import BytesIO
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 导入图片库 【注意】需要安装库: pip install Pillow
# 导入库
from PIL import Image
from selenium.webdriver.common import keys

options = webdriver.ChromeOptions()
# 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument(
    'user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Mobile Safari/537.36')

# 进入浏览器设置
browser = webdriver.Chrome('./chromedriver', options=options)
# 请求的网站
browser.get('https://qzone.qq.com/')
# 隐式等待
browser.implicitly_wait(30)
# 输入账号密码
# 等待, 查到该元素时
wait = WebDriverWait(browser, 5)
until = wait.until(EC.presence_of_element_located((By.ID, 'u')))
print('找到元素: ', until)
browser.find_element_by_id('u').send_keys('495212365')
browser.find_element_by_id('p').send_keys('a456123.')
# 点击登录
browser.find_element_by_id('go').click()
time.sleep(10)
# Num = 0
#
# Num += 1
# print(Num)
# browser.execute_script('var q=document.documentElement.scrollTop=900')
# 下拉至 页面底部
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

while True:
    try:
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="赞"]')))
        like = browser.find_element_by_xpath('//button[text()="赞"]')
        print(like)

        top = int(like.location["y"])

        # 浏览器下拉到点赞位置
        browser.execute_script('document.documentElement.scrollTop={}'.format(top))
        # 模拟真实鼠标点击事件

        ActionChains(browser).move_to_element(like).click().perform()



    except Exception as e:
        print(e)
        print('下拉到页面底部')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        load_most = browser.find_element_by_xpath('//button[text()="加载更多"]')
        print(load_most)
        # load_most.click()
        ActionChains(browser).move_to_element(load_most).click().perform()
    # # 找出元素的坐标
# left = int(like.location["x"])
#     top = int(like.location["y"])
# 浏览器下拉到点赞位置
#     browser.execute_script('document.documentElement.scrollTop={}'.format(top))
# time.sleep(5)
# full_img_png = browser.get_screenshot_as_png()
# full_img = Image.open(BytesIO(full_img_png))
# full_img.save('全屏截图.png')
#
# right = left + int(like.size["width"]) + 500
# bottom = 0 + int(like.size["height"]) + 500
#
# cut_info = (left, 0, right, bottom)
#
# print(cut_info)

# print('页面所有赞已经点击')
# time.sleep(20)


# 截图
# cut_img =  full_img.crop(cut_info)
# 保存截图内容
# cut_img.save('点击目标截图.png')
# time.sleep(3)
# 关闭浏览器
# browser.close()
# print(like)
# like.click()
#
# # 点击加载更多
# browser.find_element_by_xpath('//button[@class="btn js_morebtn"]').click()
# time.sleep(0.5)
