# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 16:25
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 大屏签到自动标记2.0.py
# @Software: PyCharm
import requests
import time
import re
import redis
import random

from tools import Log, timer


class OA_operat(object):

    def __init__(self, **kwargs):
        redis_pool = redis.ConnectionPool(host = '10.30.44.187', port = 6379, db = 6, decode_responses = True)
        redis_conn = redis.Redis(connection_pool = redis_pool)
        self.redis = redis_conn

        self.proxies = {'http':  f'http://ceshi:ceshi@139.9.196.110:708{random.randint(0, 3)}',
                        'https': f'http://ceshi:ceshi@139.9.196.110:708{random.randint(0, 3)}'}
        self.log = Log()
        self.sleep = kwargs.get('sleep', 10)
        Cookie = self.redis.get('Cookie')
        X_CSRF_TOKEN = self.redis.get('X_CSRF_TOKEN')
        self.headers = {'Accept':       'application/json,text/plain,*/*',
                        'Cookie':       Cookie,
                        'User-Agent':   'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/96.0.4664.45Safari/537.36Edg/96.0.1054.29',
                        'X-CSRF-TOKEN': X_CSRF_TOKEN,
                        }

    def get_oa(self):
        url = 'http://oa.douwangkeji.com/monitor/alert/info'
        resp = requests.get(url, headers = self.headers, proxies = self.proxies)
        data = resp.json()['data']['data']
        self.data_list = []
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
            resp = requests.post(url, headers = self.headers, data = data, proxies = self.proxies)
            if '操作成功' in str(resp.json()):
                self.log.info(f'{data_["name"]} 批量签到成功')

    def sign_soved_batch(self):
        for data_ in self.data_list_:
            monitor_rules_id = re.findall(r'monitor_rules_id=(\d+)&', data_['url'])[0]
            id_list = self.redis.get('id_list')
            id_list = eval(id_list)
            if int(monitor_rules_id) in id_list:
                data = {"is_select_all": 1, "monitor_rule_id": monitor_rules_id, "id": []}
                url = 'http://oa.douwangkeji.com/monitor/alert/batch-mark-test-solved'
                resp = requests.post(url, headers = self.headers, data = data, proxies = self.proxies)
                if '标记成功' in str(resp.json()):
                    self.log.info(f'{data_["name"]} 标记测试已解决')

    def auto_sign_run(self):
        while True:
            start = int(time.time())
            self.get_oa()
            self.sign_order_batch()
            self.log.info(f'执行一轮任务耗时: {int(time.time()) - start}秒')
            timer.countdown(self.sleep)

    def auto_sign_soved(self):
        while True:
            start = int(time.time())
            self.get_oa()
            self.sign_soved_batch()
            self.log.info(f'执行一轮任务耗时: {int(time.time()) - start}秒')
            timer.countdown(self.sleep)
