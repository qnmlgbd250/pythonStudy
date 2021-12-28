# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 20:01
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学17.py
# @Software: PyCharm
import requests
import execjs
import time
import base64
import hashlib
import httpx


def get_res(page):
    url = f'https://match.yuanrenxue.com/api/match/17?page={page}'
    print(url)
    headers = {
            'User-Agent': 'yuanrenxue.project',
            'Cookie':     'sessionid=zw4oza29odxmd0e7zldv4al230e1b5l3'
    }
    with httpx.Client(headers = headers, http2 = True) as client:
        response = client.get(url)
        print(response.text)

        return response.json()


if __name__ == '__main__':
    sum_ = 0
    for page_num in range(1, 6):
        time.sleep(1)
        res = get_res(page_num)
        for i in res['data']:
            sum_ += i['value']
    print(sum_)
