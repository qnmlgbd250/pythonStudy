# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 9:16
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 微博评论.py
# @Software: PyCharm

import requests

mid = '4704993863270514'
max_id = 0
count = 200
flow = 0
is_asc = 1

headers = {
                'accept': 'application/json, text/plain, */*',
        }
params = {
                "flow":             flow,
                "is_reload":        1,
                "id":               mid,
                "is_asc":           is_asc,
                "is_show_bulletin": 2,
                "is_mix":           0,
                "max_id":           max_id,
                "count":            count
        }
comments = requests.get('https://weibo.com/ajax/statuses/buildComments',headers=headers, params = params)
print(comments.text)