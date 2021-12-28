# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 17:32
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 阿里巴巴爬虫.py
# @Software: PyCharm
import requests
import json

headers = {
        'referer':            'https://detail.1688.com/',
        'user-agent':         'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/96.0.4664.55Safari/537.36Edg/96.0.1054.43',
}

res = requests.get('https://laputa.1688.com/offer/ajax/widgetList.do?callback=jQuery17209427418233117795_1638956285652&data=offerdetail_ditto_title%2Cofferdetail_common_report%2Cofferdetail_ditto_serviceDesc%2Cofferdetail_ditto_preferential%2Cofferdetail_ditto_postage%2Cofferdetail_ditto_offerSatisfaction%2Cofferdetail_w1190_guarantee%2Cofferdetail_w1190_tradeWay%2Cofferdetail_ditto_whosaleself&offerId=658201676984',headers=headers)

data = json.loads(res.text.replace('jQuery17209427418233117795_1638956285652(','').replace(')',''))
print(data)