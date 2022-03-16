# -*- coding: utf-8 -*-
# @Time    : 2021/12/9 17:55
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 订单标记.py
# @Software: PyCharm
import requests

headers = {'aaccept': 'application/json', 'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
           'content-type': 'application/x-www-form-urlencoded',
           'cookie': '_m_h5_tk=628544985fefe5e69b82a20175806d54_1647358471355;  _m_h5_tk_enc=8a38605f2f26ab82f259f1c836678e4d; cna=QwB/Geb80zcCAXjlW12Xj/LN; xlly_s=1; isg=BC0t-vL4M7zUK9dQUQLwfsmzPMmnimFcFdsBa28xGUQz5k2YN9s3LHT30boA43kU',
           'origin': 'https://h5.m.goofish.com', 'referer': 'https://h5.m.goofish.com/',
           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"', 'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-site',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}

params = {'jsv': '2.5.8', 'appKey': '12574478', 't': '1647349611527', 'sign': '7448965c0f6c0ce6ee5528c9da965253',
          'api': 'mtop.taobao.idle.awesome.detail', 'v': '1.0', 'dataType': 'json', 'valueType': 'string',
          'preventFallback': 'true', 'type': 'json', 'data': '{"itemId":"670539526494"}'}

response = requests.get('https://h5api.m.goofish.com/h5/mtop.taobao.idle.awesome.detail/1.0/?',
                        headers = headers, params = params)
print(response.text)
