# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 18:24
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学05.py
# @Software: PyCharm

import requests
import execjs
import time
import base64
import hashlib

def get_res(page_num,parm):
    mf = f'm={parm[-2]}&f={parm[-1]}'
    url = f'https://match.yuanrenxue.com/api/match/5?page={page_num}&{mf}'
    print(url)
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookie':f'sessionid=88zabnq2b7qdvgtx19doanng3tie0def;m={parm[0]}; RM4hZBv0dDon443M={parm[1]}'
    }
    response = requests.get(url=url,headers=headers)
    print(response.json())
    return response.json()

def calculate_m_value():
    with open('05.js',mode='r',encoding='utf-8') as f:
        JsData = f.read()
    cookie_value = execjs.compile(JsData).call('get_m_value')
    return cookie_value


if __name__ == '__main__':
    sum_ = []
    for page_num in range(1, 6):
        time.sleep(1)
        if page_num == 1:
            cookie_value = [0,0,0,0]
        else:
            cookie_value = calculate_m_value()
        res = get_res(page_num, cookie_value)
        for i in res['data']:
            sum_.append(i['value'])
    b = 0
    for j in sorted(sum_)[-5:]:
        b += j
    print(b)


