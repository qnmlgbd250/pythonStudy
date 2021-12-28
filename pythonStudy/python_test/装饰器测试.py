# -*- coding: utf-8 -*-
# @Time    : 2021/8/29 22:15
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 装饰器测试.py
# @Software: PyCharm
import time

# def out(canshu):
#     def cehi(func):
#         def wrapper(*args,**kwargs):
#             # 可以理解为闭包中的global,在内部函数中修改外部函数的值
#             nonlocal canshu
#             while int(canshu) < 100:
#                 start= time.time()
#                 time.sleep(1)
#                 content = func(*args,**kwargs)
#                 print('本次用时%s' % (time.time()-start))
#                 canshu = int(canshu) + 1
#                 # 被装饰的函数有返回值的情况下需要返回
#                 if canshu >= 100:
#                     return content
#                 else:
#                     return wrapper
#         return wrapper
#     return cehi
#
#
# @out(canshu=30)
# def xx():
#     print(123)
#
# xx()


# import schedule, functools, time
#
#
# def run_every(freq = 1, time_unit = 'minute'):
#     '''定时任务装饰器'''
#
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 func(*args, **kwargs)
#             except:
#                 pass
#         return wrapper
#
#     return decorator
#
# @run_every(freq=1)
# def xx():
#     print(123)
#
# xx()

# def every(func):
#
#     def wrapper(*args, **kwargs):
#         # args是一个数组，kwargs一个字典
#         logging.warn("%s is running" % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper


def every(timing):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while timing < 100:
                time.sleep(1)
                print('小于100秒')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@every(30)
def foo(name='foo'):
    print("i am %s" % name)

foo()

