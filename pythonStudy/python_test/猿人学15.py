# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 22:03
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学15.py
# @Software: PyCharm
import requests
import pywasm
import time
import math
import random

def get_res(page_num,parm):
    url = f'https://match.yuanrenxue.com/api/match/15?'
    print(url)
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookie':'sessionid=z77lik6rru4szxjzzl5avg50h79f69t8'
    }
    params = {
            'm':parm,
            'page':page_num
    }
    response = requests.get(url=url,headers=headers,params = params)
    print(response.json())
    return response.json()

def get_m():
    t1 = int(time.time() / 2)
    t2 = int(time.time() / 2 - math.floor(random.random() * 50 + 1))
    ws = pywasm.load('main.wasm')
    m = ws.exec('encode', [t1, t2])
    return str(m) + '|' + str(t1) + '|' + str(t2)

if __name__ == '__main__':
    sum_ = 0
    for page_num in range(1, 6):
        time.sleep(1)
        m = get_m()
        res = get_res(page_num, m)
        for i in res['data']:
            sum_ += i['value']
    print(sum_)
