# -*- coding: utf-8 -*-
# @Time    : 2021/11/25 17:20
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 猿人学19.py
# @Software: PyCharm
import requests
import urllib3
import httpx
import json
from hyper import HTTP20Connection


def get_res(page):
    url = f'https://match.yuanrenxue.com/api/match/19?page={page}'
    headers = {
            'User-Agent': 'yuanrenxue.project',
            'Cookie':     'sessionid=xtv0ieisy2870st6s2ulfm9p3axgek6f',
    }
    httpx._config.DEFAULT_CIPHERS = 'TLS_AES_128_GCM_SHA256:LS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES256-GCM-SHA384:AES256-SHA'
    with httpx.Client(headers = headers, http2 = True) as client:
        response = client.get(url)
        print(response.text)

        return response.json()


def get_response(page):
    import requests
    from hyper.contrib import HTTP20Adapter

    s = requests.Session()
    s.mount('https://match.yuanrenxue.com/api/match/17', HTTP20Adapter())
    r = s.get('https://match.yuanrenxue.com/api/match/17')
    print(r.text)

def get_resss(page):
    import requests
    # from requests import packages
    # from requests.packages.urllib3.util import Retry
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA'
    headers = {
            'User-Agent': 'yuanrenxue.project',
            'Cookie':     'sessionid=agaugex3fili9rszyts3m33nmmkoy614',
    }
    requests = requests.session()
    url2 = f'https://match.yuanrenxue.com/api/match/19?page={page}'
    response = requests.get(url2,headers=headers)
    print(response.status_code)
    print(response.json())
    return response.json()


if __name__ == '__main__':
    sum_ = 0
    for page_num in range(1, 6):
        res = get_res(page_num)
        for i in res['data']:
            sum_ += i['value']
    print(sum_)
