# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 14:05
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : Caches.py
# @Software: PyCharm

import os
import configparser
from python_test.config.settings import BASE_PATH, CACHES
from peewee import *
import datetime

db = SqliteDatabase(os.path.join(BASE_PATH, 'runtime', 'cache', 'caches.db'))


class cache(Model):
    id = AutoField()
    key = CharField(verbose_name = '缓存键名', unique = True)
    value = CharField(verbose_name = '缓存配置')
    create_time = DateTimeField(verbose_name = '创建时间', default = datetime.datetime.now())

    class Meta:
        database = db
        db_table = "caches"


class FileCache(object):

    def __init__(self, *args, **kwargs):

        # 获取根目录
        self._path = BASE_PATH

        # 创建目录
        if not os.path.exists(os.path.join(self._path, 'runtime')):
            os.makedirs(os.path.join(self._path, 'runtime'))

        # 创建缓存目录
        if not os.path.exists(os.path.join(self._path, 'runtime', 'cache')):
            os.makedirs(os.path.join(self._path, 'runtime', 'cache'))

        _path = os.path.join(self._path, 'runtime', 'cache')

        self._file_data = {
                'file_name': 'file_caches.ini',
                'section':   'caches'
        }

        if CACHES in ['sqlite']:
            cache.create_table()

    def set(self, _key, _value):
        """
        :param _key: 键名
        :param _value: 内容
        :return:
        """
        if CACHES in ['ini']:
            return self.__set_config_file(_key, _value)
        elif CACHES in ['sqlite']:
            try:
                re = cache.get_or_none(cache.key == _key)
                if re is None:
                    return cache.create(key = _key, value = _value).save()
                else:
                    re.value = _value
                    return re.save()
            except Exception as _error:
                return False

        return False

    def delete(self, _key):
        if CACHES in ['ini']:
            return self.__delete_config_file(_key)
        elif CACHES in ['sqlite']:
            result = cache.get_or_none(cache.key == _key)
            if result is None:
                return True
            return cache.delete().where(cache.key == _key).execute()
        return False

    def get(self, _key, default = None):
        """
        :param _key: 键名
        :param default 默认值
        :return:
        """
        result = None
        if CACHES in ['ini']:
            result = self.__get_config_file(_key)
        elif CACHES in ['sqlite']:
            result = cache.get_or_none(cache.key == _key)
            if result is None:
                return default
            return result.value
        if result is None:
            return default
        return result

    def __set_config_file(self, key, value):
        try:
            path = os.path.join(self._path, self._file_data['file_name'])
            _config = configparser.ConfigParser()
            _config.read(path)
            if _config.sections() in [[]]:
                _config.add_section(self._file_data['section'])
            _config.set(self._file_data['section'], key, str(value))
            with open(path, "w+") as f:
                _config.write(f)
                return True
        except Exception:
            return False

    def __get_config_file(self, _key):
        try:
            path = os.path.join(self._path, self._file_data['file_name'])
            _config = configparser.ConfigParser()
            _config.read(path)
            try:
                return _config.get(self._file_data['section'], _key)
            except Exception:
                return None
        except Exception:
            return None

    def __delete_config_file(self, _key):
        try:
            path = os.path.join(self._path, self._file_data['file_name'])
            _config = configparser.ConfigParser()
            _config.read(path)
            try:
                _config.remove_option(self._file_data['section'], _key)
                with open(path, "w+") as f:
                    _config.write(f)
                    return True
            except Exception:
                return None

        except Exception:
            raise Exception('get file caches failure', )


f_cache = FileCache()
