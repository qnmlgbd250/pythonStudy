# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 14:03
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : appConfig.py
# @Software: PyCharm

import sys
from typing import Dict, Any

from python_test.public.Env import env
from python_test.public.GetPath import get_project_path

# NeedDo 配置数据后面需改用枚举，否则数据多可能会重名覆盖数据
# NeedFix 每个人的编辑器的格式化代码风格略有不同，提交代码时会花费检查格式化代码的时间，需统一代码格式


configs: Dict[Any, Any] = {}

# 平台cookie回调时间
configs.update(
        dict(cookies_call_back_time = 20 * 60)
)

# cookies脚本配置
configs.update(dict(cookies = {
        # 指定加载的平台,优先级最高
        'platformBase.load':           {
                'jq',
        },
        # 忽略加载的平台
        'platformBase.blacklist.load': {
                'jq'
        }
}))

# 不需要登录的平台:
configs.update(dict(
        no_need_login = ['gspingtai', 'xinyue', 'chaoshidai', 'mieba']
))

# 对方平台退单成功后，立即删除订单，无法找到订单记录的平台名称:
configs.update(dict(
        order_info_deleted_immediately = ['diyidouyin', 'jindaohang', 'jingpinwangluo', 'guakebao', 'hongtu']
))

# 服务器运行所在的服务器名称
configs.update(dict(server_name = env('data', 'server_name', 'localhost')))

# 监控中心配置项
configs.update(dict(monitoring_center = {
        'app_id':  env('monitoring-center', 'app_id', None),
        'app_key': env('monitoring-center', 'app_key', None),
        'url':     env('monitoring-center', 'url', None)
}))

# 不需要乘以单位的平台
configs.update(dict(
        special_goods_id = []
))

# 退款操作后的等待时间
configs.update(dict(
        refund_waiting_time = 3 * 60
))

# 下单排队状态的等待时间，时间未到不调用下单函数
configs.update(dict(
        order_wait_times = 60 * 5
))

configs.update(dict(times = {
        'sleep': int(env('data', 'sleep', 10)),  # 循环的通用间隔
}))

# 订单分配配置
configs.update(dict(distributionOrder = {
        # 等待时间
        'waitingTime': env('data', 'waitingTime', 10),
        # 开启队列模式
        'queue':       True,
}))

# 平台数据,中控配置
configs.update(dict(mark_id = {
        'desktop': env('data', 'desktop_mark_id', '')
}))

# 需要处理评论审核商品  # 358,1058
configs.update(dict(process_commid_goods = '358'))

# 采集mark_id
configs.update(dict(
        collection_mark_id = env('data', 'collection_mark_id', ''),
        order_mark_id = env('data', 'order_mark_id', ''),
        price_mark_id = env('data', 'price_mark_id', ''),
        refund_mark_id = env('data', 'refund_mark_id', '')
))

# 单价监控和自动改价的平台
configs.update(dict(
        wechat_goods_id = [  # 微信平台，用于自动改价
                '64', '105', '106', '298', '299', '300', '304', '305', '306', '307', '308', '309',
                '317', '318', '319', '327', '328', '329', '330', '338', '366', '367', '368', '369',
                '370', '371', '372', '376', '377', '378', '379', '380', '381', '382', '383', '384',
                '385', '387', '390', '391', '392', '393', '394', '395', '464', '467', '468', '579',
                '580', '593', '595', '616', '624', '668', '769', '804', '812', '813', '814', '815',
                '816', '817', '818', '819', '838', '839', '915', '916', '932', '933', '934', '935',
                '936', '937', '938', '939', '936', '937', '938',
                '1295', '1296', '1297', '1298', '1299', '1300', '1279', '1287', '1288', '1634'
                # '972'
        ],
        price_goods_id = [  # 维护和下架状态也上执行单价监控，用于自动改价和下架功能
                '366', '367', '368', '369', '370', '838', '839', '915', '916',
                '932', '933', '934', '935', '936', '937', '938', '939', '1279',
                '1295', '1296', '1297', '1298', '1299', '1300', '1287', '1288',
                '770', '1030', '1349', '1350', '1351', '1352', '631', '1967', '1968'
        ],
        price_platform = ['xiongmao', 'gorilla', 'gspingtai', 'sumei', 'hufenzhijia', 'dyzhushou']

))

# 不进行操作的商品id
configs.update(dict(goods_blacklist = eval(env('data', 'blacklist', '{}')), ))

# 不进行操作的平台
configs.update(dict(blacklist_platform = eval(env('data', 'blacklist_platform', '[]'))))

# 执行平台名
configs.update(dict(
        platformarray = eval(env('data', 'platformarray', '[]')),
))

# 执行线程数
configs.update(dict(
        collection_thread_num = env('data', 'collection_thread_num', '1'),
))

# 获取本地环境名
configs.update(dict(
        environment = env('data', 'environment', '')
))

# 是否回调已刷数
configs.update(dict(
        need_refresh_cache = True if env('data', 'refresh_cache', 'True') == 'True' else False
))

# 采集已刷数需要排队的平台
configs.update(dict(
        platform_queue_list = ['bodian', 'guakebao', 'xiongmao', 'shujuzhongxin', 'weidan', 'taitan']
))

# 特殊平台需要每次生成token
configs.update(dict(special = ['jq', 'xiongying']))

# 应用名称
configs.update(dict(appname = 'newPlatform'))

# 有开始数的二级分类
configs.update(dict(start_params_type = [4, 5, 6, 7, 10,  # 微博

                                         ]))

# 二次检测
configs.update(
        dict(second_check = {
                'count': 3,
                'platform_name':
                         ['jq', 'weidan', 'fengyun', 'bodian', 'qidian', 'liuliangtuiguang', 'niuniu', 'diyidouyin',
                          'xiongmao',
                          'hongtu', 'guakebao', 'diandian', 'dianfeng', 'guakebao', 'lunhuizhijing', 'yile', 'jianyou',
                          'shidai', 'taitan',
                          'jingpinwangluo', 'for', 'zhongchuang', 'mayi', 'sumei', 'xiaohao', 'weilian', 'huli',
                          'liunian', "hongtunew", "guakebao", "xinbang", "yiw", "fengniao", "fenfen", "dyzhushou",
                          "weitui", "jindaohang", "baidupingtai", "luban", "hongjia", "jiayi", "caihong", 'weizhizao',
                          "huanyingguanglin", "wusi", "qilu", "qianmeng", "huoyuan", "dailishua", "xinxing", "chuyin",
                          "qiangwei", "uuwangluo", "yisanba", 'hongmeng', 'forever', 'chengzi', 'uuyile',
                          'caihonghuoyuan', 'bole', 'ddlaozs','xiangda','aimer','xixishequ']
        })
)

# 日志配置
configs.update(dict(log = {"global": {
        'sink':       sys.stdout,
        'format':     "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                      "| <level>{level: <8}</level> | "
                      "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                      " - <level>{message}</level>",
        'catch':      True,
        'enqueue':    True,
        'filter':     [],
        'activation': [("my_module.secret", False), ("another_library.module", False)]
},
        # 注意改动以下的任一sink改动会影响Log.py中日志的正则命名
        'info':                      {
                'sink':     get_project_path() + '/runtime/{time:YYYY}{time:MM}/{time:DD}/info_{time:DD}.log',
                'format':   "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                            "| <level>{level: <8}</level> | "
                            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                            " - <level>{message}</level>",
                'catch':    True,
                'enqueue':  True,
                'rotation': '200MB',
                'mode':     'a',
                'encoding': 'utf-8',
        },
        'success':                   {
                'sink':     get_project_path() + '/runtime/{time:YYYY}{time:MM}/{time:DD}/success_{time:DD}.log',
                'format':   "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                            "| <level>{level: <8}</level> | "
                            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                            " - <level>{message}</level>",
                'catch':    True,
                'enqueue':  True,
                'rotation': '200MB',
                'mode':     'a',
                'encoding': 'utf-8',
        },
        'warn':                      {
                'sink':     get_project_path() + '/runtime/{time:YYYY}{time:MM}/{time:DD}/warn_{time:DD}.log',
                'format':   "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                            "| <level>{level: <8}</level> | "
                            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                            " - <level>{message}</level>",
                'catch':    True,
                'enqueue':  True,
                'rotation': '200MB',
                'mode':     'a',
                'encoding': 'utf-8',
        },
        'exception':                 {
                'sink':     get_project_path() + '/runtime/{time:YYYY}{time:MM}/{time:DD}/error_{time:DD}.log',
                'format':   "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                            "| <level>{level: <8}</level> | "
                            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                            " - <level>{message}</level>",
                'catch':    True,
                'enqueue':  True,
                'rotation': '200MB',
                'mode':     'a',
                'encoding': 'utf-8',
        },
        'error':                     {
                'sink':     get_project_path() + '/runtime/{time:YYYY}{time:MM}/{time:DD}/error{time:DD}.log',
                'format':   "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                            "| <level>{level: <8}</level> | "
                            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                            " - <level>{message}</level>",
                'catch':    True,
                'enqueue':  True,
                'rotation': '200MB',
                'mode':     'a',
                'encoding': 'utf-8',
        }}
)
)
