# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 14:09
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : Env.py
# @Software: PyCharm

import os
import configparser
from typing import Union

from python_test.public.GetPath import get_project_path

# 获取根目录
env_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 调用此处必须要了解ini的配置格式

def env(key, value, default=None):
    """
    :param key:
    :param value: 英文字母只能小写
    :param default:
    :return:
    """
    array = {}
    configs = configparser.ConfigParser()
    configs.read(os.path.join(env_path, 'env.ini'))
    if not configs.sections():
        configs.read(os.path.join(env_path, 'env.ini'))
    for keys in configs.sections():
        temporary = {}
        for key_ in configs[keys]:
            temporary.update({key_: configs.get(keys, key_)})
        array.update({keys: temporary})
    return array.get(key, {}).get(value, default)


def env_is_dev(environment=None):
    """
    用于判断当前环境，再确定是否运行
    :param environment:
    :return:
    """
    environment = environment or env('data', 'environment', 'dev')
    if environment == 'prod':
        return False
    if environment == 'test':
        return False
    if environment == 'dev':
        return True


if __name__ == '__main__':
    # while True:
    print(env('inside', 'url', 111))
    pass
