# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 11:00
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 请求头格式化.py
# @Software: PyCharm

s ='''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: general_sessions=hru544elq8tvndf707ds0q1all0djngn; Hm_lvt_7e2ffda08048aa3ac3115e202bdd11fb=1640573150; Hm_lpvt_7e2ffda08048aa3ac3115e202bdd11fb=1640578144
if-modified-since: Mon, 27 Dec 2021 04:09:03 GMT
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62
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


