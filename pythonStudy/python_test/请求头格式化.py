# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 11:00
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 请求头格式化.py
# @Software: PyCharm

s ='''
url: https://mp.weixin.qq.com/s/-nG1oUm8dzeOjn4hos9RMg
plan_num: 10
type: 1
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




