import re
from io import BytesIO
import pytesseract
from   PIL import Image
from selenium import webdriver
import time



browser = webdriver.Chrome('./chromedriver')
browser.implicitly_wait(10)
# 浏览器最大化
browser.maximize_window()
browser.get("http://sh.ziroom.com/z/vr/61592968.html")
time.sleep(5)
full_image = browser.get_screenshot_as_png()

full_img = Image.open(BytesIO(full_image))
full_img.save('自如详情页.png')

price_element = browser.find_element_by_xpath('//span[@id="room_price"]')
print(price_element)
# 获取截图的4个点
location = price_element.location
left = int(location["x"])
top = int(location["y"]) + 2
size = price_element.size
right = left + int(size["width"])
bottom = top + int(size["height"])

# 构建截图
cut_info = (left,top,right,bottom)
print(cut_info)

# 截取识别图片
img = full_img.crop(cut_info)
img.save("价格截图.png", config='chi_sim')

browser.quit()

# 识别图片
img_str = pytesseract.image_to_string(img)
print(img_str)
print(re.findall('\d+', img_str)[0])