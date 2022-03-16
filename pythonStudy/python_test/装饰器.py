# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 20:09
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 装饰器.py
# @Software: PyCharm
import time


def Timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f'测试{func.__name__}耗时{time.time() - start}')
        return ret
    return wrapper


@Timer
def foo(name='foo',a = 'nnnjn'):
    print("i am %s" % name,a)

if __name__ == '__main__':
    foo()