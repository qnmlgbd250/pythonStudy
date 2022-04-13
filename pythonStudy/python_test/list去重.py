# -*- coding: utf-8 -*-
# @Time    : 2022/2/13 13:39
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : list去重.py
# @Software: PyCharm
# def delList(L):
#     for i in L:
#         if L.count(i) != 1:
#             for x in range((L.count(i) - 1)):
#                 L.remove(i)
#     return L
#
#
# print(delList([1, 2, 2, 3, 3, 4, 5]))
# print(delList([1, 8, 8, 3, 9, 3, 3, 3, 3, 3, 6, 3]))

# try:
# 	# 使用raise抛出异常
# 	raise IndexError("下标越界")
# except IndexError as e:
# 	pass                 #这里可以恢复代码
# except (TypeError, NameError):
# 	pass                 # 很多别的异常可以在这里处理
# else:                    # 可选，其他异常
# 	blocks
# 	print("All good!")   # 没有异常情况
# finally:                 #  无论如何都会执行的
# 	print("这里执行所有的代码，无论是否有异常")

# from threading import Thread
# import time
#
# g_num = 1000
#
#
# def work1():
#     global g_num
#     g_num += 3
#     print("work1----num:", g_num)
#
#
# def work2():
#     global g_num
#     print("work2---num:", g_num)
#
#
# if __name__ == '__main__':
#     print("start---num:", g_num)
#     t1 = Thread(target = work1)
#     t1.start()
#
#     # 故意停顿一秒，以保证线程1执行完成
#     time.sleep(1)
#
#     t2 = Thread(target = work2)
#     t2.start()


# print(sum([i for i in range(1,101)]))
# print(sum([i for i in range(1,101)]))

# dd = {"Peter": 100, "Alice": 88, "Ben": 333}
# del dd['Peter']
# print(dd)
#
# cc = {'lihua':19}
# dd.update(cc)
# print(dd)

# def f(x):
#     return x*x
# a = [1,2,3,4,5]
# b = list(map(f,a))
# print(b)

# c = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
# print(c)

# print(r'\t\r')
# print('\t\r')
# print(R'\t\r')

# c = lambda x,y: x*y
# print(c(4,5))

# li = [1,2,3,4,5,6,7,8,9,10,11,12,15,19]
# new_list = filter(lambda a:a % 2 == 1,li)
# print(list(new_list))
# #filter第一个参数为空，将获取原来序列

# import re
# str1 = '<div class="hejdhnjefl">中国</div>'
# nam = re.findall(r'<div class="[A-Za-z0-9]+">(.*?)</div>',str1)
# print(nam)

# a = [1,2,3]
# b = [4,5,6]
# print(a+b)

# strs = '123456'
# print(strs.find('9'))

# import re
# str1 = "Python's features"
# str2 = re.match( r'(.*)on(.*?) .*', str1, re.M|re.I)
# print (str2.group(1))

# class Person:
#     def __init__(self):
#         pass
#     def getAge(self):
#         print (__name__)
# p = Person()
# p.getAge()

# k = 1000
# while k > 1:
#     print (k)
#     k = k/2

# def chanageList(nums):
#     nums.append('c')
#     print("nums", nums)
# str1 = ['a', 'b']
# # 调用函数
# chanageList(str1)
# print("str1", str1)

# tup = (('onion','apple'),('tomato','pear'))
#
# for _,fruit in tup:
#
#     print(fruit)

# def fn():
#
#     t = []
#
#     i = 0
#
#     while i < 2:
#
#         t.append(lambda x: print(i*x,end=","))
#
#         i += 1
#
#     return t
#
# for f in fn():
#
#     f(2)


# strs = 'abbacabb'
# print(strs.strip('ba'))

# list1 = [1,2,3,4,5,6]
# a = list1[-1:1:-1]
# print(a)

# str1 = "exam is a example!"
# str2 = "exam"
# print(str1.find(str2, 7))

# def fun(a,*,b):
#
#     print(b)
#
# fun(1,2,3,4)

# a = [['1','2'] for i in range(2)]
#
# b = [['1','2']]*2
#
# a[0][1] = '3'
#
# b[0][0] = '4'
#
# print(a,b)

# print([2] in [1, 2, 3])
# for i in range(5):
#     i+=1
#     print("-------")
#     if i==3:
#         continue
#     print(i)

# str_ = input()
# str__ = str_.split()
# print(len(str__[-1]))

# str_ = 'hjAXGjajjkxn jkahk ajkh '
# s = 'J'
# t = str_.upper().strip().count(s.upper())
# print(t)

# while True:
#     try:
#         l = input()
#         for i in range(0, len(l), 8):
#             print("{0:0>8}".format(l[i:i + 8]))
#     except:
#         break

# n = float(input())
# y = lambda x : int(x+0.5)
# print(y(n))
#
# print(int(3.7))

# data = []
# while True:
#     try:
#         d = []
#         l = input()
#         for i in range(int(l)):
#             d.append(int(input()))
#         data.append(d)
#     except (EOFError,KeyboardInterrupt,ValueError):
#         break
# for da in data:
#     d_ = list(set(da))
#     for i in sorted(d_):
#         print(i)

# 进制转换
# while True:
#     try:
#         s=input()
#         print(int(s,16))
#     except:
#         break

# 质因数
# import math
# n = int(input())
# for i in range(2, int(math.sqrt(n))+1):
#     while n % i == 0:
#         print(i, end=' ')
#         n = n // i
# if n > 2:
#     print(n)

# 合并表记录
# dic = {}
# n = int(input())
# while True:
#     try:
#         line = input()
#         tmp = line.split()
#         index = int(tmp[0])
#         value = int(tmp[1])
#         if index in dic:
#             dic[index] += value
#         else:
#             dic[index] = value
#     except:
#         break
# for k, v in sorted(dic.items()):
#     print(f'{k} {v}')

# 提取不重复的整数
# a = input()
# a = a[::-1]
# num=[]
# for i in a:
#     if i in num:
#         continue
#     else:
#         num.append(i)
#         print(i,end='')

# 重复字符
# s = 'abfftty'
# t = []
# for i in s:
#     t.append(i)
# e = set(t)
# print(len(list(e)))


# 选出列表里面最大值的索引
# arr = [24,69,100,99,79,78,67,36,26,19]
# a = [24,0]
# j = 0
# for i in arr[1:]:
#     if i > a[0]:
#         j += 1
#         a[0] = i
#         a[1] = j
#     else:
#         continue
# print(a[0])
# print(a[1])
# print(arr.index(a[0]))

# 合并两个长度相同的列表成一个字典
# def merge_list(a:list,b:list):
#     c = dict(zip(a,b))
#     print(c)
# merge_list([1,2,3],['a','b','c'])

# 字符串反转
# str='Runoob'
# print(str[::-1])

# str='Runoob'
# print(list(reversed(str)))
# print(''.join(reversed(str)))


# if __name__ == '__main__':
# print(hex(16))  # 转换一个整数对象为十六进制的字符串
# print(oct(16))  # 转换一个整数对象为八进制的字符串
# print(bin(16))  # 转换一个整数对象为二进制字符串
# print(chr(65))  # 转换一个[0, 255]之间的整数为对应的ASCII字符
# print(ord('A'))  # 将一个ASCII字符转换为对应整数
# print(int('0x10', 16))  # 16进制转10进制
# print(int('0o10', 8))  # 8进制转换10进制
# print(int('0b1010', 2))  # 2进制转10进制


# class someError(Exception):
#     pass
#
# try:
#     if '1' != 1:
#         raise someError
#     else:
#         print("someError has not occured")
# except someError:
#     print ("someError has occured")

# a = 1
# b = 2
# a = a + b
# b = a - b
# a = a - b
# print ('a = {0}, b = {1}'.format(a,b))
#
# a = 1
# b = 2
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print ('a = {0}, b = {1}'.format(a, b))

# 整数反转
# def revert(str_, p_or_n = False):
#     str_ = str(str_)  # 字符串转换
#     negative = True if str_.startswith('-') else False  # 判断是否负值
#     if negative:
#         str_ = str_.replace('-', '')
#     str__ = ''.join(reversed(str_))
#     while str__.startswith('0'):
#         str__ = str__.replace('0', '')
#     if (p_or_n and not negative) or (not p_or_n and negative):
#         str__ = '-' + str__
#     print(str__)
#
#
# if __name__ == '__main__':
#     revert(9902, False)

# import json
# a = json.dumps({'你好':'python'},ensure_ascii=False)
# print(a)
# # {"你好": "python"}
#
# import json
# a = json.dumps({'你好':'python'})
# print(a)
# # {"\u4f60\u597d": "python"}

# 99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%s * %s = %s" % (j, i, i * j), end = "  ")
#     print("  ")
# print("\n".join("\t".join(["%s*%s=%s" % (x, y, x * y) for y in range(1, x + 1)]) for x in range(1, 10)))

# list1 = [-1,-10,3,8,25]
# list1.sort(reverse=False)
# print(list1)  # 直接修改list1
#
# list1 = [-1,-10,3,8,25]
# list2 = sorted(list1,reverse=False)
# print(list2)  # 排序完之后返回一个新对象

# 绝对值排序
# foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
# foo_ = sorted(foo, key = lambda x: (x < 0, abs(x)))  # x<0时 按照绝对值从小到大排序
# print(foo_)

# 列表嵌套字典排序
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},
#  {"name":"wa","age":17},{"name":"df","age":23}]
#
# foo_ = sorted(foo,key=lambda x: x['age'],reverse=True)
# foo__ = sorted(foo,key=lambda x: x['name'],reverse=True)
# print(foo_,foo__)

# 列表嵌套元组排序
# foo = [('zs', 19), ('ll', 54), ('wa', 17), ('df', 23)]
# foo_ = sorted(foo,key=lambda x: x[0],reverse=True)
# foo__ = sorted(foo,key=lambda x: x[0],reverse=True)
# print(foo_,foo__)

# 字典按照键排序

# dic = {"name": "zs", "sex": "man", "city": "bj"}
# foo = dic.items()
# foo = [i for i in foo]
# print("字典转成列表嵌套元组", foo)
# b = sorted(foo, key = lambda x: x[0])
# print("根据键排序", b)
# new_dic = {i[0]: i[1] for i in b}
# print("字典推导式构造新字典", new_dic)

# 字符串长度排序
# foo = ['aa','abcv','s','ccc']
# foo_ = sorted(foo,key=lambda x: len(x))
# print(foo_)
#
# foo.sort(key = len)
# print(foo)

# .求两个列表的交集、差集、并集
# a = [1, 2, 3, 4]
# b = [4, 3, 5, 6]
#
# jj1 = [i for i in a if i in b]  # 在a中的i，并且在也b中，就是交集
# jj2 = list(set(a).intersection(set(b)))
#
# bj1 = list(set(a).union(set(b)))  # 用union方法
#
# cj1 = list(set(b).difference(set(a)))  # b中有而a中没有的
# cj2 = list(set(a).difference(set(b)))  # a中有而b中没有的
#
# print('交集', jj1)
# print("交集", jj2)
# print("并集", bj1)
#
# print("差集", cj1)
# print("差集", cj2)


# #找相同和不同的元素
# A = [1,2,3]
# B = [1,7,8]
# print(set(A)&set(B))
# print(set(A)^set(B))
#

# 字符串反转
# s = 'asjkhakj'
# def func(s):
#     result = ""
#     max_index = len(s)-1
#     for index,value in enumerate(s):
#         result += s[max_index-index]
#     return result
# result = func(s)
# print(result)

# 分割成字典
# str1 = "k:1|k1:2|k2:3|k3:4"
# def str2dict(str1):
#     dict1 = {}
#     for iterms in str1.split('|'):
#         key, value = iterms.split(':')
#         dict1[key] = value
#     return dict1
#
# print(str2dict(str1))
#
# # 字典推导式
# d = {k: int(v) for t in str1.split("|") for k, v in (t.split(":"),)}
# print(d)

# 去空格
# s = ' hkjhjkh '
# print(s)
# def trim1(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s
# print(trim1(s))
#
#
# def trim2(s):
#     if s[:1] == ' ':
#         s = trim2(s[1:])
#     if s[-1:] == ' ':
#         s = trim2(s[:-1])
#     return s
# print(trim2(s))
#
# def trim3(s):
#     while s[0] == ' ':
#         s = s[1:]
#     while s[-1] == ' ':
#         s = s[:-1]
#     return s
# print(trim3(s))

# 装饰器
# import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         time0 = time.time()
#         ret = fn(*args, **kw)
#         time1 = time.time()
#         print('%s executed in %s ms' % (fn.__name__, time1-time0))
#         return ret
#     return wrapper
# @metric
# def test():
#     print('测试')
#
# test()

# 带参数的装饰器
# import logging
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warning("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
#
#     return decorator
#
# @use_logging(level="warn")
# def foo(name='foo'):
#     print("i am %s" % name)
#
# foo()

# 二维数组排序
# foo = [['a1', 'b1', 'c1', 'd1'], ['a2', 'b2', 'c2', 'd2'], ['a3', 'b3', 'c3', 'd3']]
# foo_ = sorted(foo, key = lambda x: x[2], reverse = True)
# print(foo_)
#
# foo__ = [foo[2],foo[1],foo[0]]
# print(foo__)

# dict = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
# foo_ = sorted(dict.items(), key = lambda x: x[0], reverse = False)
# print(foo_)
# new_dict = {}
# for i in foo_:
#     new_dict[i[0]] = i[1]
# print(new_dict)

alist = [1, 2, 3, 1, 1, 3, 4, 5, 1, 7, 1, 3, 4, 8, 9]
astr = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
a_str = ' not found 404 张三 深圳'


def f_list(list_: list):
    list_to_set = set(list_)
    new_list = list(list_to_set)
    print(new_list)


def f_list_2(list_: list):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    print(new_list)


def f_list_3(list_: list):
    for i in list_:
        if list_.count(i) != 1:
            for x in range((list_.count(i) - 1)):
                list_.remove(i)
    print(list_)


def count_str(str_):
    from collections import Counter
    d_connter = Counter(str_)
    print(d_connter)


def op_str(str_):
    one_str_list_ = set(str_)
    one_str_list = list(one_str_list_)
    one_str_list.sort(reverse = False)
    one_str = ''.join(one_str_list)
    print(one_str)


def op_list_str(list_str):
    import re
    list_ = list_str.split(' ')
    ret = re.findall(r'\d+|[a-zA-z]+', list_str)
    for i in ret:
        if i in list_:
            list_.remove(i)
    end_str = ''.join(list_)
    print(end_str)


def fitter_(list_):
    new_fitt = filter(lambda s: s % 2 == 1, list_)
    print(list(new_fitt))


def op_list01(list_):
    new_list = [i for i in list_ if i % 2 == 1]
    print(new_list)


def op_list02(list1, list2):
    list1.extend(list2)
    list1.sort(reverse = False)
    print(list1)


def op_time():
    import datetime
    now_time = str(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '星期：' + str(datetime.datetime.now().isoweekday()))
    print(now_time)


def op_exception():
    try:
        for i in range(1, 10):
            if i > 2:
                raise Exception('数字大于2了')
    except Exception as e:
        print(e)


def op_list03(list1):
    # list_ = [e for list1_ in list1 for e in list1_]
    list_ = sum(list1, [])
    print(list_)


def op_list04():
    x = 'abc'
    y = 'def'
    z = ['d', 'e', 'f']

    print(x.join(y))
    print(x.join(z))


def op_list04(list_):
    new_list = []
    while len(list_) > 0:
        min_ = min(list_)
        list_.remove(min_)
        new_list.append(min_)
    print(new_list)


def op_str01(str_, num_):
    print(round(float(str_), num_))


def op_dict(dict_, key_):
    # dict_.pop(key_)
    del dict_[key_]
    print(dict_)


foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]


def op_list04(list_):
    foo_ = sorted(list_, key = lambda x: (x < 0, abs(x)))
    print(foo_)


def find_max_index(list_):
    max_index = 0
    list_index = 0
    for i in list_:
        if i > list_[max_index]:
            max_index = list_index
        list_index += 1
    print(max_index)


def op_list05(list_):
    foo_ = sorted(list_, key = lambda x: (x['age'], x['name']))
    print(foo_)


if __name__ == '__main__':
    op_list05([{"name": "zs", "age": 19}, {"name": "ll", "age": 54},

               {"name": "wa", "age": 19}, {"name": "df", "age": 23}])