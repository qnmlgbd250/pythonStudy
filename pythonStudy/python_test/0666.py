# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 14:37
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 0666.py
# @Software: PyCharm


import requests
import time
from Naked.toolshed.shell import execute_js, muterun_js

headers = {
        'Accept':           'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':  'gzip, deflate',
        'Accept-Language':  'zh-CN,zh;q=0.9',
        'Host':             'match.yuanrenxue.com',
        'Proxy-Connection': 'keep-alive',
        'Referer':          'http://match.yuanrenxue.com/match/6',
        'User-Agent':       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie':           'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1637370267,1637768977; sessionid=wlz52g3j8849g54yjqkxg1uqn93ecqkz; qpfccr=true; no-alert3=true'
}

session = requests.session()
session.headers = headers

for page in range(1, 6):
    t = str(int(time.time()) * 1000)

    '''第一种传参方式，按请求次数对应'''
    q = str(page) + '-' + t + '|'
    js_result = muterun_js('0666.js', t + ' ' + str(page))

    '''第二种传参方式，每次都算第一次请求'''
    # q = str(1) + '-' + t + '|'
    # js_result = muterun_js('6_js回溯.js',t+' '+str(1))

    m = js_result.stdout.strip()

    if page == 1:
        params = (
                ('m', m),
                ('q', q),
        )
    else:
        params = (
                ('page', page),
                ('m', m),
                ('q', q),
        )
    if page > 3:
        headers['User-Agent'] = 'yuanrenxue.project'
    url = 'http://match.yuanrenxue.com/api/match/6'

    response = session.get(url, params = params).json()
    print(response)
