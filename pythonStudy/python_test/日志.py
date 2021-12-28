# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 16:51
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 日志.py
# @Software: PyCharm
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021/9/27 11:34
# software: PyCharm
from loguru import logger
import sys
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
APP_NAME = 'python_test'
APP_PATH = os.path.join(BASE_DIR, APP_NAME)
RUNTIME_DIR = os.path.join(APP_PATH, 'runtime')
logger.configure(
        **{"handlers":   [
                {
                        "sink":    sys.stdout,
                        "format":  "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                                   "| <level>{level: <8}</level> | process:<green>{process}</green> |"
                                   " <level>{message}</level>",
                        "enqueue": True,
                        'catch':   True,
                },
                {
                        "sink":      os.path.join(APP_PATH, RUNTIME_DIR) + "/{time:YYYY}{time:MM}/{time:DD}/" + 'default.log' ,
                        "format":   "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                                    "| <level>{level: <8}</level> | process:<green>{process}</green> |"
                                    " <level>{message}</level>",
                        "enqueue":  True,
                        'catch':    True,
                        'rotation': '200MB',
                        'mode':     'a',
                        'encoding': 'utf-8',
                },
        ],

                "extra": {"user": "someone"}
        })

logger.info('this is another debug message')

