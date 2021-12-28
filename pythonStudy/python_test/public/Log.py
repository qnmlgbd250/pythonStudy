# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 13:22
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : Log.py
# @Software: PyCharm

import os
import re
import sys
from loguru import logger
from typing import Union

from python_test.config.settings import BASE_PATH
from python_test.public.Caches import f_cache
from python_test.public.GetPath import get_project_path

try:
    # 获取根目录
    path: Union[bytes, str] = os.path.abspath('../..')
    # 设置工作环境
    sys.path.append(path)
    from python_test.config.appConfig import configs as local_configs
except ModuleNotFoundError:
    # 获取根目录
    path: Union[bytes, str] = os.path.abspath('..')
    # 设置工作环境
    sys.path.append(path)
    from python_test.config.appConfig import configs as local_configs

# NeedFix 采集已刷数在多线程情况下会出现日志重复打印问题，但不会丢失日志

"""
1.全局配置
固定handlers参数：sink(日志记录位置=sys.stderr)、format(日志样式)、catch(捕获异常=True)、enqueue(支持并发=True)、mode(文件的打开模式)、encoding(文件的编码格式)
固定其他参数：levels(打印的级别，默认info)
可选参数：filter(过滤字符，此处用于打印)
2.局部配置，
固定参数：sink(需要区分各级别日志)、format(日志样式)  # error和warn同样放同一日期下同一文件
可选参数：error日志容量默认200MB、warn日志容量默认200MB、compression(用于压缩info日志，未确定需求)、filter(过滤字符，此处用于记录)
"""


class LogStream(object):
    """
    用于获取日志流
    """

    def __init__(self):
        self.logs = ''

    def write(self, _log):
        self.logs = ''
        self.logs += _log

    def flush(self):
        pass

    def __str__(self):
        return self.logs


class Log:
    def __init__(self, current_file = None, write_file = True):
        """

        Args:
            current_file:
            write_file:  是否写到文件
        """
        if not current_file:
            current_file = f_cache.get('run_function', 'run')  # 改为读取在启动run时缓存到本地的运行文件名
        self.current_file = current_file
        self.global_config = local_configs['log']['global']
        self.info_config = local_configs['log']['info']
        self.success_config = local_configs['log']['success']
        self.warn_config = local_configs['log']['warn']
        self.exception_config = local_configs['log']['exception']
        self.error_config = local_configs['log']['error']
        self.diy_config = None
        self.write_file = write_file
        self.info_logger = None
        self.success_logger = None
        self.error_logger = None
        self.warn_logger = None
        self.diy_logger = None

        # 用于获取error日志流
        self.log_stream = LogStream()

    def set_file_name(self, name):
        self.current_file = name

    def _get_sink(self, log_config):
        if log_config.get('name', '') == 'diy':
            return log_config['sink']

        _match = re.search('([_a-zA-Z]+).py', self.current_file)
        current_name = _match.group(1) + '_' if _match else 'not_py_file'
        _match = re.search('/([a-z]+_{time:DD}.log)', log_config['sink'])

        if _match:
            sink_str = _match.group(1)
            log_sink = re.sub('/([a-z]+_{time:DD}.log)', '/' + current_name + sink_str, log_config['sink'])
            return log_sink

    def __logger_add(self, level,judge=False):
        logger.remove()
        logger.configure(
                handlers = [
                        {
                                'sink':    self.global_config['sink'],
                                'format':  self.global_config['format'],
                                'catch':   self.global_config['catch'],
                                'enqueue': self.global_config['enqueue'],
                                'filter':  lambda log_obj: not any(
                                        [fs in log_obj['message'] for fs in self.global_config['filter']])
                        }
                ],
                activation = self.global_config['activation'],
        )

        level_config = {
                'info':      self.info_config,
                'success':   self.success_config,
                'warn':      self.warn_config,
                'error':     self.error_config,
                'diy':       self.diy_config,
                'exception': self.exception_config
        }

        if self.write_file:
            logger.add(
                    sink = BASE_PATH + "/runtime/{time:YYYY}{time:MM}/{time:DD}/" + self.current_file + "_{time:DD}.log",
                    format = level_config[level]['format'],
                    catch = level_config[level]['catch'],
                    enqueue = level_config[level]['enqueue'],
                    filter = lambda record: record['extra'].get('name') == level,
                    rotation = level_config[level]['rotation'],
                    mode = level_config[level]['mode'],
                    encoding = level_config[level]['encoding'],
            )
        if judge:
            logger.remove(handler_id = None)
            logger.add(
                    sink=BASE_PATH + "/runtime/{time:YYYY}{time:MM}/{time:DD}/" + self.current_file + "_{time:DD}.log",
                    level="INFO",
                    enqueue=True,
                    format = level_config[level]['format'],
                    catch = level_config[level]['catch'],
                    # filter = lambda record: record['extra'].get('name') == level,
                    rotation = level_config[level]['rotation'],
                    mode = level_config[level]['mode'],
                    encoding = level_config[level]['encoding'],
            )


    def diy(self, log_name, _msg, log_level = 'info'):
        self.diy_config = {
                'sink':     get_project_path() + '/runtime/{time:YYYY}{time:MM}/{time:DD}/%s.log' % log_name.replace(
                        '.log',
                        ''),
                'format':   "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                            "| <level>{level: <8}</level> | "
                            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                            " - <level>{message}</level>",
                'catch':    True,
                'enqueue':  True,
                'rotation': '200MB',
                'mode':     'a',
                'encoding': 'utf-8',
                'name':     'diy'
        }
        self.__logger_add('diy')
        self.diy_logger = logger.bind(name = 'diy')
        log_func = {'info':    self.diy_logger.info,
                    'success': self.diy_logger.success,
                    'warn':    self.diy_logger.warning,
                    'error':   self.diy_logger.error}
        return log_func[log_level](_msg)

    def info(self, _msg):
        self.__logger_add('info')
        self.info_logger = logger.bind(name = 'info')
        self.info_logger.info(_msg)

    def success(self, _msg):
        self.__logger_add('success')
        self.success_logger = logger.bind(name = 'success')
        self.success_logger.success(_msg)

    def warn(self, _msg):
        self.__logger_add('warn')
        self.warn_logger = logger.bind(name = 'warn')
        self.warn_logger.warning(_msg)

    def error(self, _msg):
        """
        :param _msg:
        :return: error日志的字符串
        """
        self.__logger_add('error')
        self.error_logger = logger.bind(name = 'error')
        self.error_logger.add(self.log_stream, level = 'ERROR')
        self.error_logger.error(_msg)
        return self.log_stream

    def exception(self, _msg):
        """

        Args:
            _msg:

        Returns:

        """
        self.__logger_add('exception')
        self.error_logger = logger.bind(name = 'exception')
        self.error_logger.add(self.log_stream, level = 'ERROR')
        self.error_logger.exception(_msg)
        return self.log_stream

    def writer_log(self,msg):
        self.__logger_add("success",True)
        self.warn_logger = logger.bind(name = 'success')
        self.warn_logger.success(msg)


log = Log(write_file = False)

if __name__ == '__main__':
    log.info(12312312312)
