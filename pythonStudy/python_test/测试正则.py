# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 9:40
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 测试正则.py
# @Software: PyCharm
import re
import json
import time

# text = 'callbackvote_query({"code":"0","content":{"pointsRemain":89.672,"pubTime":"2021-12-22 09:37:59","remark":"","title":"","userName":"86q9","url":"https://v.douyin.com/8RLRduU/","addNum":0,"user_code":"02K64FMU885KPV8X","readPerMin":0,"price":0.49,"perfPrice":0.0,"startNum":"","currentNum":"","startTime":"","id":"20211222093759712842","endTime":"","exp":"","busi_code":"","taskNum":50,"status":"0"},"msg":"下单成功"})'
#
# a = re.findall(r'callbackvote_query\((.*?)\)',text)[0]
# a = json.loads(a)
# print(int(round(time.time() * 1000)))
# print(a['msg'])
# print(a)

# a = [1,2,3,4]
#
# while a != []:
#     b = a.pop()
#     print(a)

# import random
#
# print(random.randint(0,3))

import os
import sys
if __name__== '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    # sys.path.append(BASE_DIR)
