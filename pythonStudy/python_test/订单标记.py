# -*- coding: utf-8 -*-
# @Time    : 2021/12/9 17:55
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 订单标记.py
# @Software: PyCharm
import requests

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
    'Accept': 'application/json',
    'Authorization': 'Bearer {{token}}',
}

data = {
  'tid': '2112091754399290213'
}

response = requests.post('https://trade.hulihuzhu.com/api/seller/trade/orders/:oid/supplier-status/start-buy', headers=headers, data=data)
print(response.text)