# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 11:18
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 测试微风.py
# @Software: PyCharm
import requests

headers = {
        'Accept':          'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'ApiAuth':         '01a0927a17582cda1b1de646f6fe74f4',
        'Connection':      'keep-alive',
        'Content-Length':  '258',
        'Content-Type':    'application/json;charset=UTF-8',
        'Host':            'api.wbpm3.cc',
        'Origin':          'http://api.wbpm3.cc',
        'Referer':         'http://api.wbpm3.cc/',
        'User-Agent':      'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/96.0.4664.55Safari/537.36Edg/96.0.1054.43',
}
data = {"flag":        "", "category_id": 3, "url": "https://m.weibo.cn/6084319649/4633162125410754", "number": 100,
        "good_id":     10007, "sleep": 0, "oid": "4633162125410754", "loading": False, "start_number": 2133,
        "screen_name": "你现在才20多岁，一无所有很正常，迷茫彷..."}
import json
resp = requests.post('http://api.wbpm3.cc/jiedan/Good/buy', headers = headers, data = json.dumps(data))
print(resp.text)
