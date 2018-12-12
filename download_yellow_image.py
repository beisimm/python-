import requests
from lxml import etree
import threading


def get_image(image_url, title, Num):
    print('开始下载图片: ', Num)
    image_bytes = requests.get(image_url).content
    # 这里的umei可以替换成自己创建文件夹名
    with open('./umei/%s_%s.jpg' % (title, Num), 'wb') as f:
        f.write(image_bytes)
    print('下载完成: ', Num)


# 自己筛选喜欢的url替换
url = "http://www.194mu.com/htm/pic1/124699.htm"

html = requests.get(url).content.decode()

eroot = etree.HTML(html)

# 获取标题做文件名
title = eroot.xpath('//h1/text()')[0]

# 获取图片地址链接
image_url_list = eroot.xpath('//img/@src')

Num = 0

for image_url in image_url_list:
    Num += 1
    threading.Thread(target=get_image, args=(image_url, title, Num)).start()
