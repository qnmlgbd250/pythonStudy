# -*- coding:utf-8 -*-
# @Time    : 2019/4/8 15:33
# @Author  : Brady
# @File    : Http.py
# @Software: PyCharm
# @Contact : bradychen1024@gmail.com
import json
import chardet
import traceback
from functools import wraps
import requests, time
from requests_html import HTMLSession, HTML

from python_test.public.Code import Code
from python_test.public.Log import Log

"""
1.支持css、xpath选择器进行解析
2.支持get、post请求
3.支持session请求
4.采用装饰器统一管理请求异常
"""


# def statistics_url_request(func):
#     """
#     url请求统计
#     Args:
#         func: 请求方法装饰上去
#
#     Returns:
#
#     """
#
#     @wraps(func)
#     def wrapper(self, *args, **kwargs):
#         func_name = func.__name__
#         try:
#             output = {}
#             url = [urls for urls in args if isinstance(urls, str) if urls.startswith("http")] or kwargs.get("url", None)
#             url = url[0] if isinstance(url, list) else url
#             output.update({
#                     'method': func_name,
#                     'url':    url,
#             })
#             start_time = time.time()
#             result = func(self, *args, **kwargs)
#             output['consuming'] = result.get('elapsed', None) if result.get('elapsed', None) else round(
#                     time.time() - start_time, 6)
#             self.Logger.writer_log(json.dumps(output))
#             return result
#         except Exception as _error:
#             self.Logger.exception(_error)
#             return {'code':     Code.code(102), 'msg': f'{func_name} url请求统计出现异常：{_error}',
#                     'response': f'url:{self.url}\nheader:{self.header}\n{traceback.format_exc()}'}
#
#     return wrapper


# NeedDo 增加允许自定义是否要重定向
def http_error_handle(func):
    """
    request异常处理装饰器
    :param func: 需装饰的request函数
    :return: {code: 自定义状态码, msg: 异常原因, response: url&header&error_str}
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        func_name = func.__name__
        try:
            return func(self, *args, **kwargs)
        except Exception as error:
            error_str = str(error)
            if 'Caused by ConnectTimeoutError' in error_str or 'timed out' in error_str:
                return {'code': Code.code(110), 'msg': Code.msg(110), 'response': error_str}
            elif 'Failed to establish a new connection' in error_str:
                return {'code': Code.code(10010), 'msg': Code.msg(10010), 'response': 'url:{0}\nheader:{1}\n{2}'
                    .format(self.url, str(self.header), error_str)}
            elif '远程主机强迫关闭' in error_str:
                return {'code': Code.code(10011), 'msg': Code.msg(10011), 'response': 'url:{0}\nheader:{1}\n{2}'
                    .format(self.url, str(self.header), error_str)}
            elif 'Remote end closed connection' in error_str:
                return {'code':     Code.code(10012), 'msg': Code.msg(10012),
                        'response': 'url:{0}\nfunc_name:{1}\nheader:{2}\n{3}'
                                        .format(self.url, func_name, str(self.header), error_str)}
            elif 'Exceeded 30 redirects' in error_str:
                return {'code':     Code.code(10013), 'msg': Code.msg(10013),
                        'response': 'url:{0}\nfunc_name:{1}\nheader:{2}\n{3}'
                                        .format(self.url, func_name, str(self.header), error_str)}
            return {'code':     Code.code(102), 'msg': f'{func_name} 出现异常：{error_str}',
                    'response': f'url:{self.url}\nheader:{self.header}\n{traceback.format_exc()}'}

    return wrapper


class Request:
    def __init__(self):
        self.session = HTMLSession()
        self.url = ''
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                     '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        self.Logger = Log("Http")

    def __session_request(self, url, method, data = None, header = None, params = None, cookies = None, proxies = None,
                          allow_redirects = True, verify = None, timeout = 120, **kwargs) -> dict:
        self.url = url
        if header:
            self.header = header
        if isinstance(cookies, str):
            self.header.update({'Cookie': cookies.replace('cookie: ', '')})
            response = getattr(self.session, method)(self.url, headers = self.header, params = params, data = data,
                                                     proxies = proxies, allow_redirects = allow_redirects,
                                                     verify = verify, timeout = timeout, **kwargs)
        else:
            response = getattr(self.session, method)(self.url, headers = self.header, params = params, data = data,
                                                     cookies = cookies, proxies = proxies,
                                                     allow_redirects = allow_redirects,
                                                     verify = verify, timeout = timeout, **kwargs)
        response.close()
        resp_code = response.status_code
        if 20000 + resp_code in Code.error_http_code():
            self.header.update({'Cookie': ''})  # 移除cookie
            return {'code': Code.http_code(resp_code), 'msg': Code.http_msg(resp_code), 'response': response.text}
        check_encoding = chardet.detect(response.content)
        str_encoding = check_encoding.get('encoding') if check_encoding['confidence'] > 0.9 else None
        response_text = response.content.decode(str_encoding) if str_encoding else response.text
        html_response = response.html if response_text else None

        try:
            if str_encoding:
                response_json = response.json(encoding = str_encoding)
            else:
                response_json = response.json()
        except json.decoder.JSONDecodeError:
            response_json = '非json格式的源码'

        response_cookies = response.cookies.get_dict()
        return {'code':    0, 'msg': 'success', 'response': response_text, 'content': response.content,
                'json':    response_json, 'html_response': html_response,
                'Cookie':  response_cookies, 'header': response.headers, 'url': getattr(response, 'url', '无请求页的url'),
                'elapsed': response.elapsed.total_seconds()}

    def __request(self, url, method, data = None, header = None, params = None, cookies = None, proxies = None,
                  allow_redirects = True, verify = None, timeout = 120, **kwargs) -> dict:
        self.url = url
        if header:
            self.header = header

        if isinstance(cookies, str):
            self.header.update({'Cookie': cookies.replace('cookie: ', '')})
            response = getattr(requests, method)(self.url, headers = self.header, params = params, proxies = proxies,
                                                 allow_redirects = allow_redirects, verify = verify,
                                                 timeout = timeout, **kwargs)
        else:
            response = getattr(requests, method)(self.url, headers = self.header, params = params, data = data,
                                                 cookies = cookies, proxies = proxies,
                                                 allow_redirects = allow_redirects,
                                                 verify = verify, timeout = timeout, **kwargs)
        response.close()
        resp_code = response.status_code
        if 20000 + resp_code in Code.error_http_code():
            return {'code':    Code.http_code(resp_code), 'msg': Code.http_msg(resp_code), 'response': response.text,
                    'content': response.content, 'resp': response}
        check_encoding = chardet.detect(response.content)
        str_encoding = check_encoding.get('encoding') if check_encoding['confidence'] > 0.9 else None
        response_text = response.content.decode(str_encoding) if str_encoding else response.text

        try:
            response_json = json.loads(response_text)
        except json.decoder.JSONDecodeError:
            response_json = '非json格式的源码'
        response_cookies = response.cookies.get_dict()

        return {'code':             0, 'msg': 'success', 'response': response_text, 'content': response.content,
                'json':             response_json,
                'html_response':    HTML(html = response.content) if response.content else '源码为空',
                'Cookie':           response_cookies, 'header': response.headers,
                'url':              getattr(response, 'url', '无请求页的url'),
                'request_response': getattr(response, 'request', '无请求信息'),
                'elapsed':          response.elapsed.total_seconds(),
                'resp':             response
                }

    # @statistics_url_request
    @http_error_handle
    def session_get(self, url, header = None, params = None, cookies = None, proxies = None,
                    allow_redirects = True, verify = None, timeout = 120, **kwargs) -> dict:
        """
        自带解析源码功能的get会话请求，返回带有HTML对象的字典，支持css、xpath选择器进行解析
        :param url: str类型，发送请求的链接
        :param header: dict类型，头部伪装
        :param params: dict类型，get请求的参数
        :param cookies: dict、str类型
        :param proxies: dict类型，代理
        :param allow_redirects: bool类型，是否允许重定向，默认为True
        :param verify: bool类型，是否跳过ssl证书认证
        :param timeout: int类型，默认60秒
        :return: dict
        """
        return self.__session_request(url, method = 'get', header = header, params = params, cookies = cookies,
                                      proxies = proxies,
                                      allow_redirects = allow_redirects, verify = verify, timeout = timeout, **kwargs)

    # @statistics_url_request
    @http_error_handle
    def session_post(self, url, header = None, data = None, cookies = None, proxies = None,
                     allow_redirects = True, verify = None, timeout = 120, **kwargs) -> dict:
        """
        自带解析源码功能的post会话请求，返回带有HTML对象的字典，支持css、xpath选择器进行解析
        :param url: str类型，发送请求的链接
        :param header: dict类型，头部伪装
        :param data: dict、str类型，post请求的表单参数
        :param cookies: dict、str类型
        :param proxies: dict类型，代理
        :param allow_redirects: bool类型，是否允许重定向，默认为True
        :param verify: bool类型，是否跳过ssl证书认证
        :param timeout: int类型，默认60秒
        :return: dict
        """
        return self.__session_request(url, method = 'post', header = header, data = data, cookies = cookies,
                                      proxies = proxies,
                                      allow_redirects = allow_redirects, verify = verify, timeout = timeout, **kwargs)

    # @statistics_url_request
    @http_error_handle
    def get(self, url, header = None, params = None, cookies = None, proxies = None,
            allow_redirects = True, verify = None, timeout = 120, **kwargs) -> dict:
        """
        自带解析源码功能的get请求，返回带有HTML对象的字典，支持css、xpath选择器进行解析
        :param url: str类型，发送请求的链接
        :param header: dict类型，头部伪装
        :param params: dict类型，get请求的参数
        :param cookies: dict、str类型
        :param proxies: dict类型，代理
        :param allow_redirects: bool类型，是否允许重定向，默认为True
        :param verify: bool类型，是否跳过ssl证书认证
        :param timeout: int类型，默认60秒
        :return: dict
        """
        return self.__request(url, method = 'get', header = header, params = params, cookies = cookies,
                              proxies = proxies,
                              allow_redirects = allow_redirects, verify = verify, timeout = timeout, **kwargs)

    # @statistics_url_request
    @http_error_handle
    def post(self, url, header = None, data = None, cookies = None, proxies = None,
             allow_redirects = True, verify = None, timeout = 120, **kwargs) -> dict:
        """
        自带解析源码功能的post请求，返回带有HTML对象的字典，支持css、xpath选择器进行解析
        :param url: str类型，发送请求的链接
        :param header: dict类型，头部伪装
        :param data: dict、str类型，post请求的表单参数
        :param cookies: dict、str类型
        :param proxies: dict类型，代理
        :param allow_redirects: bool类型，是否允许重定向，默认为True
        :param verify: bool类型，是否跳过ssl证书认证
        :param timeout: int类型，默认60秒
        :return: dict
        """
        return self.__request(url, method = 'post', header = header, data = data, cookies = cookies, proxies = proxies,
                              allow_redirects = allow_redirects, verify = verify, timeout = timeout, **kwargs)
