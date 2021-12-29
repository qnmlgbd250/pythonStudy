# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 16:25
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 大屏签到自动标记2.0.py
# @Software: PyCharm
import requests
import time
import math
import re
import redis
import random

from tools import Log, timer


class OA_operat(object):
    MONITOR_RULE_DICT = {
            34: '订单超过5分钟未更新(全部)',
            44: '订单开始数采集超时',
            6:  '重复检测的监控',
            3:  '拨号服务器掉线全部实例',
            17: '订单超过10分钟未更新',
            37: '订单超过3分钟未更新(全部)',
            33: '订单重复检测商品未上报检测',
            14: '订单超过3分钟未更新(全部)',
            8:  '商城订单监控-审核中数量'
    }

    def __init__(self, **kwargs):
        Cookie = 'XSRF-TOKEN=eyJpdiI6InNVV0kxcXZ4VG1jSWVUUnVxeGZSN1E9PSIsInZhbHVlIjoiU2VVTVhDdDBEN3VBdFdHWFMzZklFV3FuRGlrRUhza1wvSG16WVIyUVFvbkpFZ3lncVwvZWhSOEpLMGYzWGVzWm5aIiwibWFjIjoiYmZiYmM2M2E1ODUzMmMyMWU2NTQwMmFlYTNmYjkzYjA1MTY0Y2E5YTE4ODBiNThmNzhlMTg4YmUyYTU4NjdhNCJ9; laravel_session=eyJpdiI6InAwN0t6SmRMWEhFVGZZS1RabkYxUnc9PSIsInZhbHVlIjoiYytFRUVqRXNUUVgwU3lHbTZNQ2FRaUZzYjdGNm1pbTZqa1hwblZTaWpGOUhtbFJDSlluOGdyOXhQV2ZRRUJDYSIsIm1hYyI6IjMwOWFhOGJiZmFiZWExMzA3N2Q5OTI3MjNiODhjNjRiM2YzYmRmZTExZmU3ZDM5MjM1MWZiNGNlNzNiYjNlNDgifQ%3D%3D'

        X_CSRF_TOKEN = '6PkdPBgCHNAnI52aZKxc0TjCmnQWyPpzt377AiST'

        self.headers = {'Accept':       'application/json,text/plain,*/*',
                        'Cookie':       Cookie,
                        'User-Agent':   'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/96.0.4664.45Safari/537.36Edg/96.0.1054.29',
                        'X-CSRF-TOKEN': X_CSRF_TOKEN,
                        }
        redis_pool = redis.ConnectionPool(host = '127.0.0.1', port = 6379, db = 6, decode_responses = True)
        redis_conn = redis.Redis(connection_pool = redis_pool)
        self.redis = redis_conn

        self.monitor_rules_id_list = []  # 储存自动标记的项目id
        self.proxies = {'http':  f'http://ceshi:ceshi@139.9.196.110:708{random.randint(0, 3)}',
                        'https': f'http://ceshi:ceshi@139.9.196.110:708{random.randint(0, 3)}'}
        self.log = Log()
        self.sleep = kwargs.get('sleep', 10)

    def get_oa(self):
        """获取大屏需要签到的项目url片段和需要标记的项目id"""
        url = 'http://oa.douwangkeji.com/monitor/alert/info'
        resp = requests.get(url, headers = self.headers)
        data = resp.json()['data']['data']
        self.data_list = []  # 储存大屏告警项列表
        self.data_list_ = []
        for data_ in data['big_data'] + data['admin']:
            if data_['to_sign_in'] != 0:
                monitor_rules_id = re.findall(r'monitor_rules_id=(\d+)&', data_['url'])[0]
                if int(monitor_rules_id) in [29]:  # 有bug的项目的monitor_rules_id跳过签到
                    continue
                self.data_list.append(data_)
            if data_['to_sign_in'] == 0 and data_['number'] != '正常':
                self.data_list_.append(data_)

    def sign_order_batch(self):
        for data_ in self.data_list:
            monitor_rules_id = re.findall(r'monitor_rules_id=(\d+)&', data_['url'])[0]
            url = 'http://oa.douwangkeji.com/monitor/alert/batch-add-record'
            data = {"is_select_all": 1, "monitor_rule_id": monitor_rules_id, "id": []}
            resp = requests.post(url, headers = self.headers, data = data)
            if '操作成功' in str(resp.json()):
                self.log.info(f'{data_["name"]} 批量签到成功')

    def get_orders(self):
        """重构项目url 请求该地址获取单个项目所有告警内容"""
        for data in self.data_list:
            if data['to_sign_in'] <= 20:
                limit = 20
            else:
                limit = data['to_sign_in']
            url_new = 'http://oa.douwangkeji.com/' + data['url'].replace('monitor/list?',
                                                                         f'monitor/alert/list?page=1&limit={limit}&') + '&type=2'
            req_s = int(time.time())
            resp = requests.get(url_new, headers = self.headers,
                                proxies = self.proxies)
            self.log.info(f'请求待签到项目:[{data["name"]}] 耗时{int(time.time()) - req_s}秒 url:{url_new}')
            for order in resp.json()['data']['data']:
                if order['personnel_operate_record'] == None:
                    self.redis.lpush('to_sign_in_order', order['id'])
                else:
                    if order['monitor_rules_id'] in [37, 14, 33, 8, 3, 44, 34, 11, 29, 5, 31, 34, 42, 43, ]:
                        self.redis.lpush('monitor_rules_id_list', order['id'])

    def sign_order(self):
        """自动签到订单"""
        id_ = ''
        while id_ != None:
            id_ = self.redis.lpop('to_sign_in_order')
            if id_ == None:
                self.log.info('无告警')
                # time.sleep(5)
                # self.sign_soved()
                break
            url = f'http://oa.douwangkeji.com/monitor/alert/add-record/{id_}'
            resp = requests.post(url, headers = self.headers)
            if '不允许在转派了' in str(resp.json()):
                continue
            if '超过最大可转派时间' in str(resp.json()):
                continue
            self.log.info('签到订单')
            self.log.info(resp.json())

    def sign_soved_batch(self):
        for data_ in self.data_list_:
            monitor_rules_id = re.findall(r'monitor_rules_id=(\d+)&', data_['url'])[0]
            if int(monitor_rules_id) in [37, 14, 33, 8, 3, 44, 34, 5, 31, 34, 42, 43,20]:
                """
                22自动维护开始数  17订单10分钟 6重复检测 
                """
                data = {"is_select_all": 1, "monitor_rule_id": monitor_rules_id, "id": []}
                url = 'http://oa.douwangkeji.com/monitor/alert/batch-mark-test-solved'
                resp = requests.post(url, headers = self.headers, data = data)
                if '标记成功' in str(resp.json()):
                    self.log.info(f'{data_["name"]} 标记测试已解决')

    def sign_soved(self):
        while self.monitor_rules_id_list != []:
            _id_ = self.monitor_rules_id_list.pop()
            url = f'http://oa.douwangkeji.com/monitor/alert/mark-test-solved/{_id_}'
            url1 = f'http://oa.douwangkeji.com/monitor/alert/mark-solved/{_id_}'
            data = {"remarks": "", "img": ""}  # 已解决
            resp = requests.post(url1, headers = self.headers, data = data)
            if '标记成功' in str(resp.json()):
                self.log.info(f'{_id_} 标记测试已解决')
            else:
                continue

    def auto_sign_run(self):
        while True:
            try:
                start = int(time.time())
                self.get_oa()
                self.sign_order_batch()
                self.log.info(f'执行一轮任务耗时: {int(time.time()) - start}秒')
                timer.countdown(self.sleep)
            except:
                start = int(time.time())
                self.get_oa()
                self.get_orders()
                self.sign_order()
                timer.countdown(self.sleep)
                self.log.info(f'执行一轮任务耗时: {int(time.time()) - start}秒')

    def auto_sign_soved(self):
        while True:
            start = int(time.time())
            self.get_oa()
            self.sign_soved_batch()
            self.log.info(f'执行一轮任务耗时: {int(time.time()) - start}秒')
            timer.countdown(self.sleep)
