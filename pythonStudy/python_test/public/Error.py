# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 14:07
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : Error.py
# @Software: PyCharm

class BaseError(Exception):
    """
    基类
    """

    def __init__(self, msg = None, **kwargs):
        self.msg = msg or self.__doc__
        self.kwargs = kwargs or None

    def __str__(self):
        return self.msg


class AuthorError(BaseError):
    """验证参数失败"""


class GetConfigError(BaseError):
    """获取配置信息失败"""


class PathError(BaseError):
    """路径异常"""
