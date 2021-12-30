# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 16:16
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : redis测试.py
# @Software: PyCharm
import redis

redis_pool = redis.ConnectionPool(host = '10.30.43.115', port = 6379, db = 1,decode_responses=True,password = '123456')
redis_conn = redis.Redis(connection_pool = redis_pool)

# redis_conn.lpush('name_2', '3', '622', '4646')  # name_2 列表名字 后面元素名称
# # while True:
# a = redis_conn.lpop('name_2')
# # b = (bytes.decode(a))  # 字节转字符串
# # print(b)
# print(a)
# # print(type(b))
# print(type(a))

redis_conn.set('Cookie','XSRF-TOKEN=eyJpdiI6IlZ1SlFFdm12NkhoeGd1MnVqMnJNWmc9PSIsInZhbHVlIjoiZWxRUzd4VTQyekRoXC9hSklKVENUNVhXalNUcXhaeFpBS1wvUWVtdTRzOFlQOTVVa2dZXC9LKzdBRVRMRXVhTWdPKyIsIm1hYyI6ImMyNWIyNDc3NmQzNmFlMmVkYTdmYjQ5NmNiZTE1YjM4MDk5OTllYjgxNWI0ZTRlMTg2ODM0ZmE2NTNjMGVkYWEifQ%3D%3D; laravel_session=eyJpdiI6ImFHWXdxN2pBWlVHMVJhdkEzZGlFUWc9PSIsInZhbHVlIjoianR3UFVYSTZwaWRPMlMwUnc4RWN0TWVndTdteFwvcVpmVE1FUnZXc09JdXVNaktITmZTQ0h3VnRMc0ZPcFNFdnQiLCJtYWMiOiJlYzFhNWUwMjM5M2M0OTljODdmMjliNjFmMTQ4ODJjZjI0YzY0Nzk2MGNjZTJlMDg2ZDU0OTFjMDUwNjRiYWZjIn0%3D')

Cookie = redis_conn.get('Cookie')
print(Cookie)