# 导入模块
import re

import pytesseract
# 导入图片库 【注意】需要安装库: pip install Pillow
# 导入库
from PIL import Image

img = Image.open('test.jpg')

img_str = pytesseract.image_to_string(img, config='chi_sim')
# print(img_str)
print(re.findall('\d+', img_str)[0])