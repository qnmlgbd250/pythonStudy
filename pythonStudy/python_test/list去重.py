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

def fn():

    t = []

    i = 0

    while i < 2:

        t.append(lambda x: print(i*x,end=","))

        i += 1

    return t

for f in fn():

    f(2)
