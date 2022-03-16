# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 13:09
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学20.py
# @Software: PyCharm

import requests
import pywasm
import time
import math
import random


def get_res(page_num):
    url = f'https://match.yuanrenxue.com/api/match/20?'
    print(url)
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookie': 'sessionid=0osiu3eriq0q5km4os1nys9ykf5kvrye'
    }
    params = {'page': page_num, 'sign': 'd6d932ce54bf36a60db5972ce15a8d76', 't': '1647148121000'}
    response = requests.get(url = url, headers = headers, params = params)
    print(response.json())
    return response.json()


def get_m():
    ws = pywasm.load('wasm.wasm')
    m = ws.exec('$__wbindgen_add_to_stack_pointer', [-16],)
    print(m)
    # t1 = int(time.time() / 2)
    # t2 = int(time.time() / 2 - math.floor(random.random() * 50 + 1))
    # ws = pywasm.load('main.wasm')
    # m = ws.exec('encode', [t1, t2])
    # return str(m) + '|' + str(t1) + '|' + str(t2)


if __name__ == '__main__':
    get_m()
    # get_res('2')
    # sum_ = 0
    # for page_num in range(1, 6):
    #     time.sleep(1)
    #     m = get_m()
    #     res = get_res(page_num, m)
    #     for i in res['data']:
    #         sum_ += i['value']
    # print(sum_)
