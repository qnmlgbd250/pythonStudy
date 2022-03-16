# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 11:00
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 请求头格式化.py
# @Software: PyCharm

s ='''
jsv: 2.5.8
appKey: 12574478
t: 1647349611527
sign: 7448965c0f6c0ce6ee5528c9da965253
api: mtop.taobao.idle.awesome.detail
v: 1.0
dataType: json
valueType: string
preventFallback: true
type: json
data: {"itemId":"670539526494"}
'''



ls = s.split('\n')
lsl = []
ls = ls[1:-1]
headers = {}
for l in ls:
    l = l.split(': ')
    lsl.append(l)
for x in lsl:
    headers[str(x[0]).strip('    ')] = x[1]
print(headers)




