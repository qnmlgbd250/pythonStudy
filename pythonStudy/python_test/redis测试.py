# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 16:16
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : redis测试.py
# @Software: PyCharm
import redis

redis_pool = redis.ConnectionPool(host = '127.0.0.1', port = 6379, db = 5,decode_responses=True)
redis_conn = redis.Redis(connection_pool = redis_pool,)

redis_conn.lpush('name_2', '3', '622', '4646')  # name_2 列表名字 后面元素名称
# while True:
a = redis_conn.lpop('name_2')
# b = (bytes.decode(a))  # 字节转字符串
# print(b)
print(a)
# print(type(b))
print(type(a))
