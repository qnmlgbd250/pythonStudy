# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 16:40
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : auto_wx.py
# @Software: PyCharm
import os
import time
import win32api
import win32con

while True:
    rest = os.system('E:\WXWork\WXWork.exe')
    if rest == 0:
        time.sleep(2)
        win32api.keybd_event(0x1B, win32api.MapVirtualKey(0x1B, 0), 0, 0)
        win32api.keybd_event(0x1B, win32api.MapVirtualKey(0x1B, 0), win32con.KEYEVENTF_KEYUP, 0)
        print(1)
    else:
        continue

