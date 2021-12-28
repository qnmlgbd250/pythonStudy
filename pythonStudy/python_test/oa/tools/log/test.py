# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 8:53
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : test.py
# @Software: PyCharm
import os
import sys
if __name__== '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(BASE_DIR)
    # sys.path.append(BASE_DIR)