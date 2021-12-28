# -*- coding: utf-8 -*-
# @Time    : 2021/12/9 16:02
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学06.py
# @Software: PyCharm

import requests
import execjs
import time


def get_res(page_num, m, time_):
    param = {
            'page':page_num,
            'm': m,
            'q':    str(page_num) + '-' + str(time_) + '|'
    }
    url = f'https://match.yuanrenxue.com/api/match/6'
    print(url)
    headers = {'accept':           'application/json, text/javascript, */*; q=0.01',
               'accept-encoding':  'gzip, deflate, br',
               'accept-language':  'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
               'cookie':           'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1637370267,1637768977; sessionid=wlz52g3j8849g54yjqkxg1uqn93ecqkz; qpfccr=true; no-alert3=true',
               'referer':          'https://match.yuanrenxue.com/match/6',
               'sec-ch-ua':        '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
               'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
               'sec-fetch-mode':   'cors', 'sec-fetch-site': 'same-origin',
               'User-Agent':       'yuanrenxue.project',
               'x-requested-with': 'XMLHttpRequest'}
    response = requests.get(url = url, headers = headers,params = param)
    print(response.json())
    return response.json()


def calculate_m_value(t,p):
    with open('06.js', mode = 'r', encoding = 'utf-8') as f:
        JsData = f.read()
    cookie_value = execjs.compile(JsData.replace("\xa0","")).call('get_m_value',t,p)
    return cookie_value


if __name__ == '__main__':
    sum = 0
    for page_num in range(1, 6):
        time.sleep(1)
        t = str(int(time.time()) * 1000)
        m_t = calculate_m_value(t,page_num)
        res = get_res(page_num, m_t, t)
        for i in res['data']:
            sum += i['value'] * 24
    print(sum)
