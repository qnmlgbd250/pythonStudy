# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 13:30
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 飞鸟云注册.py
# @Software: PyCharm

from public import Http
import random
import sqlite3
import threading
from threading import Thread


class FeiNiao(object):

    def __init__(self, *args, **kwargs):
        super(FeiNiao, self).__init__(*args, **kwargs)
        self._header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.106 Safari/537.36',
        }
        self.Http = Http.Request()
        self._url = 'https://feiniaoyun.tk/api/v1/passport/auth/register'
        self.dbpath = './runtime/cache/emails.db'

    def registered(self):
        """
        注册账号
        :return:
        """
        email = self.create_email()
        data = {
            'email': f'{email}@gmail.com',
            'password': '11111111',
            'invite_code': '',
            'email_code': ''
        }
        _res = self.Http.post(self._url, header = self._header, data = data)
        if _res['code'] == 0 and _res['json']['data'] == True:
            return self.save_email_db(one_email_list = [email, '11111111'])
        else:
            return self.save_email_db(one_email_list = [email, '22222222'])

    def create_email(self):
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        suffix = random.randint(9999999, 100000000)
        return "1{}{}{}{}".format(second, third, suffix, second)

    def init_email_db(self):
        sql = '''create table if not exists email_list
                (email varchar ,
                pw varchar,
                date timestamp not null default (datetime('now','localtime')))'''
        conn = sqlite3.connect(self.dbpath)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def save_email_db(self, one_email_list):
        self.init_email_db()
        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        sql = """insert into email_list (
                       email,pw) 
                       values(%s)""" % ",".join(one_email_list)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        print(f'{one_email_list}保存数据成功')


class Tpoll(Thread):

    def __init__(self, *args, **kwargs):
        Thread.__init__(self)

    def run(self):
        FeiNiao.registered()


FeiNiao = FeiNiao()
if __name__ == '__main__':
    FeiNiao.registered()
    # c = 0
    # while c < 10:
    #     c += 1
    #     crawl_list = []
    #     for i in range(5):
    #         Crawl = Tpoll()
    #         crawl_list.append(Crawl)
    #         Crawl.start()
    #
    #     for crawl in crawl_list:
    #         crawl.join(timeout = 60)
