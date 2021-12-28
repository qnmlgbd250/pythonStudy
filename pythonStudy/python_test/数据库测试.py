# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 21:04
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 数据库测试.py
# @Software: PyCharm
import datetime
from peewee import *

DATABASES = {
        'NAME':     'test_dev',
        'USER':     'test_dev',
        'PASSWORD': 'test_dev',
        'HOST':     '10.30.43.132',
        'POST':     3306,
        'CHARSET':  'utf8mb4'

}


class OrderFlow(Model):
    # 流水类型扣费
    WALLET_TYPE_DEDUCTION = 1
    # 流水类型退款
    WALLET_TYPE_REFUND = 2

    supplier_sdk = CharField(max_length = 32, verbose_name = "供应商SDK")
    supplier_key = CharField(max_length = 32, verbose_name = "供应商")
    supplier_user_name = CharField(max_length = 32, verbose_name = "供应商账号")
    flow_type = IntegerField(verbose_name = "流水类型", null = True, default = WALLET_TYPE_DEDUCTION)
    flow_id = CharField(max_length = 64, verbose_name = "流水订单号")
    amount = CharField(max_length = 50, verbose_name = "消费金额")
    remark = CharField(max_length = 255, verbose_name = "流水备注")
    wallet = CharField(max_length = 255, verbose_name = "当前钱包金额")
    wallet_before_change = CharField(max_length = 255, verbose_name = "变动前钱包金额")
    url = CharField(max_length = 255, verbose_name = "订单地址", null = True, )
    number = CharField(max_length = 20, verbose_name = "订单数量", null = True)
    supplier_platform_id = CharField(max_length = 60, verbose_name = "供应商订单ID", null = True)
    create_at = CharField(max_length = 50, verbose_name = "流水创建时间")
    collection_at = DateTimeField(default = datetime.datetime.now(), verbose_name = '创建时间')

    class Meta:
        database = MySQLDatabase(
                database = DATABASES['NAME'],
                user = DATABASES['USER'],
                passwd = DATABASES['PASSWORD'],
                host = DATABASES['HOST'],
                port = DATABASES['POST'],
                charset = DATABASES['CHARSET']
        )
        db_table = 'supplier_flow_orders'
        verbose_name = '流水订单'
        verbose_name_plural = verbose_name
        # 设置联合主键
        unique_together = (
                ("supplier_sdk", "supplier_key", 'supplier_user_name', 'flow_type', 'flow_id'),
        )
        # 设置查询索引
        indexes = (
                ("supplier_sdk", "supplier_key"),
                ("supplier_sdk", "supplier_key", "supplier_user_name"),
                ("supplier_sdk", "supplier_key", "flow_type"),
                (
                        "supplier_sdk", "supplier_key", 'supplier_user_name', 'flow_type', 'url', 'number'
                ),
                ("supplier_sdk", "supplier_key", 'supplier_user_name', 'flow_type',
                 'supplier_platform_id'
                 ),
                ("supplier_sdk", "supplier_key", 'supplier_user_name', 'flow_type', 'remark'),

        )

    def __str__(self):
        return f"supplier_key:{self.supplier_key} user:{self.supplier_user_name} " \
               f"type:{self.flow_type} flow_id:{self.flow_id}"


boot = OrderFlow.insert_many(
        {
                'supplier_sdk':         1111,
                'supplier_key':         2222,
                'supplier_user_name':   2222,
                'flow_type':            2222,
                'flow_id':              22222,
                'amount':               33423,
                'remark':               3432123,
                'wallet':               234123,
                'wallet_before_change': 34343,
                'url':                  213423,
                'number':               23234,
                'supplier_platform_id': 2342,
                'create_at':            35436,
        }
).execute()
print("插入数据：", boot)
