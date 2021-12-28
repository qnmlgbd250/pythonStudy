# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 17:58
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 随机密码.py
# @Software: PyCharm
import math
import random

# 明文
plainstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
seclist = list(plainstr)
random.shuffle(seclist)
# 密码本
secstr = ''.join(seclist)
print("原文", plainstr, '\n密文', str(secstr))
inputstr = input("输入：")
for p in inputstr:
    if ord("a") <= ord(p) <= ord("z"):
        index = ord(p) - ord("a")
        ans = secstr[index]
        print(ans.lower(), end = '')
    elif "A" <= p <= "Z":
        index = ord(p) - ord("A")
        ans = secstr[index]
        print(ans, end = '')
    else:
        print(p, end = '')
