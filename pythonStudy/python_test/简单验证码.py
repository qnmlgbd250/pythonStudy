# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 12:00
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 简单验证码.py
# @Software: PyCharm

# import pytesseract
# from PIL import Image
#
# image = Image.open("img.png")
# result = pytesseract.image_to_string(image,lang='chi_sim')
# print(result)
# print(type(result))

# import ddddocr
# ocr = ddddocr.DdddOcr()
#
# with open("img_1", 'rb') as f:
#
#     img_bytes = f.read()
#
# res = ocr.classification(img_bytes)
#
# print(res)


# from paddleocr import PaddleOCR,draw_ocr
# # Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# # You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# # to switch the language model in order.
# ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
# img_path = './img.png'
# result = ocr.ocr(img_path, cls=True)
# for line in result:
#     print(line)
#
#
# # draw result
# from PIL import Image
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')

# import easyocr
# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('img.png',detail=0)
# print(result)


import requests
import base64
import json

print('开始识别')


# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# f = open('img_2.png', 'rb')
# img = base64.b64encode(f.read())
# params = {"image": img}
# access_token = '24.1941ce2e456627970beb64eee7b71fdf.2592000.1651754937.282335-25907849'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data = params, headers = headers)
# if response:
#     print(response.json())


# 测试代码
class Ocr(object):
    def __init__(self):
        self.url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
        self.access_token = '24.6c01138ad68495e8e2958d88577c9d62.2592000.1651924935.282335-17792970'
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}

    def get_token(self):
        url = 'https://aip.baidubce.com/oauth/2.0/token'
        params = {'grant_type': 'client_credentials', 'client_id': 'L2d1e7RZJzGZKjvT8zcWjKgD',
                  'client_secret': '6hJdWYwYj0q3GdQ0QQQe1f5X6U2j6x5h'}
        response = requests.post(url, data = params)
        print(response.json())

    def get_img_text(self, img_path):
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        response = requests.post(self.url, data = params, headers = self.headers,
                                 params = {'access_token': self.access_token})
        print(response.json())


if __name__ == '__main__':
    ocr = Ocr()
    ocr.get_token()
    ocr.get_img_text('img_2.png')
