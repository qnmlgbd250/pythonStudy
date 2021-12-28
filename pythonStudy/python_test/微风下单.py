# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 22:48
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 微风下单.py
# @Software: PyCharm

import requests
import json

_header = {
        'apiAuth':      '01a0927a17582cda1b1de646f6fe74f4',
        'User-Agent':   'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                        'like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1 ',
        'Content-Type': 'application/x-www-form-urlencoded'
}
data = {"flag":         "",
        "category_id":  3,
        "url":          'https://m.weibo.cn/6084319649/4633162125410754',
        "number":       100,
        "good_id":      10007,
        "sleep":        0,
        "oid":          "",
        "loading":      False,
        "start_number": 2335,
        "screen_name":  ""
        }

info = requests.post('http://api.wbpm3.cc/jiedan/Good/buy', data = data, headers = _header)
print(info.text)
