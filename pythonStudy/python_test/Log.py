# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 8:31
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 日志重写.py
# @Software: PyCharm

import os.path
import sys
from loguru import logger
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
APP_NAME = 'python_test'
APP_PATH = os.path.join(BASE_DIR, APP_NAME)
RUNTIME_DIR = os.path.join(APP_PATH, 'runtime')

class Log(object):

    def __init__(self, file_name = 'default') -> None:
        """
        :param file_name: 文件名称
        """
        self._logs = logger
        self._file_name = file_name

        self.__path = os.path.join(APP_PATH, RUNTIME_DIR)

        self.__path_name = self._file_name + ".logs"

    def __overload_configuration(self):
        """
        重载配置
        :return:
        """
        self._logs.remove()
        return {
            "handlers": [
                {
                    "sink":    sys.stdout,
                    "format":  "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                               "| <level>{level: <8}</level> | process:<green>{process}</green> |"
                               " <level>{message}</level>",
                    "enqueue": True,
                    'catch':   True,
                },
                {
                    "sink":     self.__path + "/{time:YYYY}{time:MM}/{time:DD}/" + self.__path_name,
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

            "extra":    {"user": "someone"}
        }

    def success(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.success(_msg)

    def warning(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.warning(_msg)

    def info(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.info(_msg)

    def debug(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.debug(_msg)

    def error(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.error(_msg)

    def exception(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.exception(_msg)

log = Log()