# -*- coding: utf-8 -*-
# @Time    : 2021/12/13 22:07
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学07.py
# @Software: PyCharm
import re
import requests
import base64
from hashlib import md5
import json
from fontTools.ttLib import TTFont
def get_():
    max_ = []
    headers = {"User-Agent": "yuanrenxue.project",
               'cookie':'sessionid=1rhesctx9zfi8qddh9ddd8x176284yym'}
    for page_num in range(1, 6):

        url = f'http://match.yuanrenxue.com/api/match/7?page={page_num}'
        ret = requests.get(url, headers = headers)
        ret_str = ret.text
        wof = base64.b64decode(ret.json()['woff'])
        with open('猿人学7.woff', 'wb') as f:
            f.write(wof)
        font = TTFont('猿人学7.woff')
        font.saveXML('猿人学7.xml')

        base_font = {'font': [
                {'name': '&#xa895;', 'value': '4', 'hex': 'ec9467393c47041e0fafff7f4a2852a8'},
                {'name': '&#xb341;', 'value': '9', 'hex': '4119e3dc64f73251d40cf1fc0323e20f'},
                {'name': '&#xb643;', 'value': '6', 'hex': 'af603543300bfc5f0e35e941d4208759'},
                {'name': '&#xb917;', 'value': '2', 'hex': '9bb92485b3e2ba4bd8a93ebbd3a0fa4e'},
                {'name': '&#xc216;', 'value': '0', 'hex': '0aef9a3385d96e7bdd1f3003669a940c'},
                {'name': '&#xc387;', 'value': '3', 'hex': 'b024173b00a3c901b6e696ba12812124'},
                {'name': '&#xc637;', 'value': '7', 'hex': '3dcfec8e26ef48730f25363da55da77a'},
                {'name': '&#xe678;', 'value': '1', 'hex': '2c0ec07331fa25dc226f1ca83561cb46'},
                {'name': '&#xf427;', 'value': '5', 'hex': '9ebca885e21990cee127d23d03acb3ac'},
                {'name': '&#xf836;', 'value': '8', 'hex': 'f9d12372b7002b9a1522dd3dd142cf70'},
        ]}
        # print(font.getGlyphOrder())
        # for i in base_font['font']:
        #     # print('uni'+i['name'][3:-1].zfill(4))0
        #     font_cmap = font['glyf'].glyphs['uni'+i['name'][3:-1]].flags
        #     # print(font_cmap)
        #     font_cmap_hex = md5(font_cmap).hexdigest()
        #     print(i['name'],font_cmap_hex)

        uni_list = font.getGlyphOrder()
        uni_list.remove('.notdef')
        for i in uni_list:
            font_cmap = font['glyf'].glyphs[i].flags
            font_cmap_hex = md5(font_cmap).hexdigest()
            for j in base_font['font']:
                if font_cmap_hex == j['hex']:
                    ret_str = ret_str.replace(i.replace('uni', '&#x'), j['value'])
        # print(ret_str)
        k = json.loads(ret_str)['data']
        for i in k:
            max_.append(i['value'].strip().replace(' ',''))
    print(max_)
    print(max(max_))

if __name__ == '__main__':
    get_()
