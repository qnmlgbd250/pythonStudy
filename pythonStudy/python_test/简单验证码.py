# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 12:00
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 简单验证码.py
# @Software: PyCharm
import pytesseract
from PIL import Image

image = Image.open("img_1.png")
result = pytesseract.image_to_string(image,lang='chi_sim')
print(result)
print(type(result))









