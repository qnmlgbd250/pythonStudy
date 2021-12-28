# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 18:06
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学16.py
# @Software: PyCharm
import requests
import execjs
import time
import base64
import hashlib

def get_res(page_num,parm):
    url = f'https://match.yuanrenxue.com/api/match/16?page={page_num}&{parm}'
    print(url)
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookie':'sessionid=vz0m0dm115ecxnuw085omf8tx7zoof61'
    }
    response = requests.get(url=url,headers=headers)
    print(response.json())
    return response.json()

def calculate_m_value():
    with open('16题js.js',mode='r',encoding='utf-8') as f:
        JsData = f.read()
    cookie_value = execjs.compile(JsData).call('get_m_value')
    return cookie_value


if __name__ == '__main__':
    sum_ = 0
    for page_num in range(1, 6):
        time.sleep(1)
        cookie_value = calculate_m_value()
        res = get_res(page_num, cookie_value)
        for i in res['data']:
            sum_ += i['value']
    print(sum_)


