# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 14:04
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : settings.py
# @Software: PyCharm

import os

import platform
from dotenv import load_dotenv

from python_test.public.GetPath import get_project_path

"""
项目路径
"""
system = platform.system()
if system in ["Windows", "Linux"]:
    BASE_PATH = get_project_path()
else:
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    load_dotenv(os.path.join(BASE_PATH, '.env'), encoding = 'gbk')
except UnicodeDecodeError as error:
    load_dotenv(os.path.join(BASE_PATH, '.env'))
except Exception as error:
    print(error)

# 资源目录
RESOURCE_DIR = os.path.join(BASE_PATH, 'resource')

"""
数据库配置
"""
DATABASES = {
        'NAME':     os.getenv('DB_DATABASE', ''),
        'USER':     os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST':     os.getenv('DB_HOST', '127.0.0.1'),
        'POST':     int(os.getenv('DB_PORT', 3306)),
        'CHARSET':  os.getenv('CHARSET', 'utf8mb4')
}

"""
REDIS配置
"""
REDIS = {
        'HOST':     os.getenv('REDIS_HOST', ''),
        'PORT':     int(os.getenv('REDIS_PORT', 6379)),
        'DB':       int(os.getenv('REDIS_DB', 1)),
        'PASSWORD': os.getenv('REDIS_PASSWORD', ''),
        'ENCODING': os.getenv('ENCODING', 'utf-8'),
}

"""
缓存方式 目前支持
    ini 
    sqlites
"""
CACHES = os.getenv('CACHES_MODEL', 'sqlite')

"""
平台配置
"""
DESKTOP_MARK_ID = os.getenv('DESKTOP_MARK_ID', None)

ABNORMAL_WORD_MARK_ID = os.getenv('ABNORMAL_WORD_MARK_ID', None)

"""
开始数配置
"""
START_GOODS_MARK_ID = os.getenv('START_GOODS_MARK_ID', None)

"""
中控配置项
"""
INSIDE_URL = os.getenv('INSIDE_URL', None)
INSIDE_APP_KEY = os.getenv('INSIDE_APP_KEY', None)
INSIDE_SECRET_KEY = os.getenv('INSIDE_SECRET_KEY', None)

SERVER_NAME = os.getenv('SERVER_NAME', 'No notes yet')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')

# cookies 回调间隔时间
COOKIES_CALL_BACK_TIME = int(os.getenv('COOKIES_CALL_BACK_TIME', 5 * 60))

# Supervisor conf path
# 进程管理的配置存放位置
SUPERVISOR_COF_PATH = os.getenv('SUPERVISOR_COF_PATH', None)

# 拨号配置
A_DSL_USER = os.getenv('A_DSL_USER', '')
A_DSL_PASS = os.getenv('A_DSL_PASS', '')
A_DSL_NAME = os.getenv('A_DSL_NAME', '宽带连接')

WEIBO_UID = os.getenv('WEIBO_UID', '')
WEIBO_GSID = os.getenv('WEIBO_GSID', '')

# 监控中心配置
MONITORING_CENTER_URL = os.getenv('MONITORING_CENTER_URL', None)
MONITORING_CENTER_APP_ID = os.getenv('MONITORING_CENTER_APP_ID', None)
MONITORING_CENTER_APP_KEY = os.getenv('MONITORING_CENTER_APP_KEY', None)

# 运行的服务器备注名称
SERVER_REMARKS = os.getenv('SERVER_REMARKS', 'No notes')

# 重新拉取配置的次数
INIT_COUNT = int(os.getenv('INIT_COUNT', 5))

# 开放平台API
DEV_API_DOMAIN = os.getenv('DEV_API_DOMAIN')
DEV_API_APP_ID = os.getenv('DEV_API_APP_ID')
DEV_API_APP_KEY = os.getenv('DEV_API_APP_KEY')

# django API
DJANGO_API_URL = os.getenv('DJANGO_API_URL', None)
DJANGO_API_TOKEN = os.getenv('DJANGO_API_TOKEN', None)

WRONG_ADDRESS_KEY = os.getenv('WRONG_ADDRESS_KEY', '0')

DY_CLIENT_ID = os.getenv('DY_CLIENT_ID', "")
# 默认一页
DY_USER_PAGE = int(os.getenv('DY_USER_PAGE', 1))

# 小红书cid
XHS_CLIENT_ID = os.getenv('XHS_CLIENT_ID', '')

# 小红书替换次数
XHS_RELOAD_COUNT = int(os.getenv('XHS_RELOAD_COUNT', 200))
# 小红书设备调用次数
XHS_PLAY_COUNT = int(os.getenv('XHS_PLAY_COUNT', 5))
DY_PLAY_COUNT = int(os.getenv('DY_PLAY_COUNT', 2))

My_Red_ID = os.getenv('My_Red_ID', '')

# 全局忽略平台
NO_EXECUTION_PLATFORM = os.getenv('NO_EXECUTION_PLATFORM', '').split(',')

# 维护转上架白名单
WHITE_LIST = os.getenv('WHITE_LIST', '').split(',')

CELERY_BROKER = os.getenv('CELERY_BROKER')
CELERY_BACKEND = os.getenv('CELERY_BACKEND')

STATISTICAL_TIME_SWITCH = os.getenv('STATISTICAL_TIME_SWITCH', 0)
# 重复检测采集个数
CONTRAST_NUMBER = os.getenv('CONTRAST_NUMBER', 3)

COOKIE_UPDATE_TIME = os.getenv('COOKIE_UPDATE_TIME', 120)

# 重复下单采集时间
CONSTRAST_TIME = os.getenv('CONSTRAST_TIME', 2 * 24 * 60 * 60)

COLLECTION_UPLOAD_FLAG = os.getenv('COLLECTION_UPLOAD_FLAG', 0)

# 忽略单价对比的平台 此处要以Class的名称来填写否则无法生效
IGNORE_UNIT_PRICE_COMPARISON = ['PingLunKeLong', 'AiYunTui', "APingTai"]

# 社区请求模式  0=>不使用API接口请求  1=>使用API接口请求
COMMUNITY_REQUEST_API_MODEL = False if int(os.getenv('COMMUNITY_REQUEST_API_MODEL', 0)) == 0 else True

EOMS_TOKEN = os.getenv("EOMS_TOKEN", "")
EOMS_URL = os.getenv("EOMS_URL", "")

SURVEILLANCE_SYSTEM_DOMAIN = os.getenv('SURVEILLANCE_SYSTEM_DOMAIN', None)
SURVEILLANCE_SYSTEM_TOKEN = os.getenv('SURVEILLANCE_SYSTEM_TOKEN', None)
os.environ.setdefault('LOAD_PROJECT_PATH', BASE_PATH)
SHOP_COLLECTION = os.getenv("SHOP_COLLECTION", "http://10.30.43.115")
