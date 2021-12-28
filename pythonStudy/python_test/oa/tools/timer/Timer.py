# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 22:35
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : Timer.py
# @Software: PyCharm
import time
import sys
import math

def countdown(timing_num: (int, float), remarks = '剩余休眠时间还有'):
    """
    不换行的倒计时打印，只限单线程情况下调用
    :param timing_num:
    :param remarks:
    :return:
    """
    time.sleep(0.01)  # 用于不跟日志打印行冲突
    # print('Task->sleep->{0}'.format(timing_num))
    if timing_num < 1:
        print(f'{remarks}:{timing_num}秒')
        time.sleep(timing_num)
        return

    if isinstance(timing_num, float):
        num_float, num_int = math.modf(timing_num)
        num_int = int(num_int)
    else:
        num_float, num_int = 0, timing_num

    for num in range(num_int, -1, -1):
        if num == 0 and num_float:
            sys.stdout.write(f'\r{remarks}:{round(num_float, 2)}秒')
            sleep_num = num_float
        else:
            sys.stdout.write(f'\r{remarks}:{num}秒')
            sleep_num = 1
        sys.stdout.flush()

        time.sleep(sleep_num)
    print('\n')