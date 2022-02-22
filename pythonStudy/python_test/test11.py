# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 11:01
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : test11.py
# @Software: PyCharm


a = [1, 5, 9, 10]
b = list(range(0, 100))

for i in b:
    if i not in a:
        b.remove(i)

print(b)
