# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 10:59
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : WeiPingTai.py
# @Software: PyCharm

import json
import re
import time
from urllib import parse
from lxml import etree
from abc import ABC

from platformBase.BaseController import BaseController
from public.Log import log
from public.Code import Code
from public.ResultHandle import ResultHandle
from config.BaseProxyConfig import ProxyBridging
from exception.Error import WalletError

rh = ResultHandle()


class WeiPingTai(BaseController, ABC):

    def __init__(self):
        super(WeiPingTai, self).__init__()
        self._header = {
                'Cookie':       '',
                'User-Agent':   'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                                'like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1 ',
                'Content-Type': 'application/x-www-form-urlencoded'
        }
        self._status = {
                '0': '创建',
                '1': '执行中',
                '2': '完成',
                '4': '申请退款',
                '3': '退款',
        }
        self.log = log

    @ProxyBridging
    @rh.result_handle
    def login(self, user = '', password = ''):
        try:
            self._header['Cookie'] = ''
            verify_text_info = self.Http.get(self._platform_url + '/index.php?s=/Login/verify', header = self._header,
                                             timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if verify_text_info['code'] != 0:
                return verify_text_info
            for key, value in verify_text_info['Cookie'].items():
                self._header['Cookie'] += '{}={}; '.format(key, value)
            verify_text = self.Ocr.discern(verify_text_info['content'], 1000)['Result']
            print(verify_text)
            formhash_info = self.Http.get(self._platform_url + '/index.php?s=/Login/', header = self._header,
                                          timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            formhash = re.findall(r'name="formhash" value="(.*?)"', formhash_info['response'])[0]
            data = {
                    'formhash':  formhash,
                    'loginname': user,
                    'password':  password,
                    'yzm':       verify_text
            }
            info = self.Http.post(self._platform_url + '/index.php?s=/Login/logaction', data = data,
                                  header = self._header, timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if info['code'] != 0:
                return info
            _info = info['response']
            if '验证码不正确' in _info:
                return {'code': Code.code(10015), 'msg': _info, 'response': _info}
            if '登录失败,用户不存在' in _info:
                return {'code': Code.code(103), 'msg': _info, 'response': _info}
            if '登录成功' in _info:
                for key, value in info['Cookie'].items():
                    self._header['Cookie'] += '{}={}; '.format(key, value)
                return {'code': Code.code(0), 'response': info['response']}
        except Exception as e:
            return {'code': Code.code(107), 'msg': f'登录错误 {e}', 'response': f'登录错误 {e}'}

    @ProxyBridging
    @rh.result_handle
    def get_money(self):
        try:
            if not self._header['Cookie'] or self._header['Cookie'] == '':
                return {'code': Code.code(108), 'response': self._header['Cookie']}
            info = self.Http.get(self._platform_url + '/index.php?s=/Index', header = self._header)
            if info['code'] != 0:
                return info
            if '请您先登录' in info['response']:
                return {'code': Code.code(108), 'msg': '未登录', 'response': info['response']}
            if '可用金额' in info["response"]:
                from lxml import etree
                html = etree.HTML(info['response'])
                money = str(html.xpath('//*[@id="fans_a"]/text()')[0])
                return {'code': Code.code(0), 'money': money, 'response': info['response']}
            else:
                return {'code': Code.code(107), 'msg': f'获取余额失败', 'response': str(info)}

        except Exception as e:
            return {'code': Code.code(107), 'msg': f'获取余额失败 {e}', 'response': f'获取余额失败 {e}'}

    @ProxyBridging
    @rh.result_handle
    def get_price(self, param):
        try:
            if not self._header['Cookie'] or self._header['Cookie'] == '':
                return {'code': Code.code(108), 'response': self._header['Cookie']}
            data = {
                    'order_num': 1000
            }
            goods_type = param['platform_goods_table']['goods_type']
            info = self.Http.post(self._platform_url + f'/index.php?s=/Index/orderadd/style_id/{goods_type}',
                                  header = self._header, data = data,
                                  timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if info['code'] != 0:
                return info
            if '商品信息' in info['response']:
                price = re.findall(r'/(\d+)元，', info['response'])[0]
                if goods_type in ['6']:
                    price = int(price) / 10000
                return {'code': 0, 'price': price, 'response': info['response']}
            else:
                return {'code': Code.code(107), 'msg': f'获取单价失败', 'response': str(info)}
        except Exception as e:
            return {'code': Code.code(107), 'msg': f'获取单价失败 {e}', 'response': f'获取单价失败 {e}'}

    @ProxyBridging
    @rh.result_handle
    def order(self, param):
        # return {'code': Code.code(104), 'msg': f'获取平台ID失败','response': ''}
        if not self._header['Cookie'] or self._header['Cookie'] == '':
            return {'code': Code.code(108), 'response': self._header['Cookie']}
        try:
            order_pid = param['platform_goods_table']['order_pid']
            order_num = param['number']
            data = {
                    'token':                self._key,
                    'timestamp':            time.time(),
                    'order_pid':            order_pid,
                    'order_num':            order_num,
                    'order_url':            param['url'],
                    'wbzv_zf_type':         order_pid,
                    'wbzv_zf_content_type': '0',
                    'wbzv_zf_content':      ''
            }
            info = self.Http.post(self._platform_url + '/index.php?s=/External/order_create', header = self._header,
                                  data = data,
                                  timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if info['code'] != 0:
                return info
            _info = info['json']

            if _info.get('error_code', None) != 0:
                return {'code': Code.code(107), 'msg': f'{_info["message"]}', 'response': f'下单结果 {_info["message"]}'}

            if 'IP' and '未授权' in str(_info):
                IP = re.findall(r'IP: (.*?) 未授权', _info['message'])[0]
                data = self.autoWhitelist(IP)
                return {'code': Code.code(107), 'msg': f'{data}', 'response': f'下单结果 {_info["message"]}'}
            if '余额不足' in str(_info):
                return {'code': Code.code(101), 'msg': f'下单失败:{_info}', 'response': str(_info)}
            if 'ok' in _info['message'] and _info['error_code'] == 0:
                platform_id = _info['data']['order_id']
                return {'code': 0, 'msg': '下单成功', 'response': str(_info), 'platform_id': platform_id}
        except Exception as e:
            return {'code': Code.code(107), 'msg': f'下单失败 {e}', 'response': f'下单失败 {e}'}

    @ProxyBridging
    @rh.result_handle
    def autoWhitelist(self, IP):
        data = {
                'ip_white_list': IP
        }
        info = self.Http.post(self._platform_url + '/index.php?s=/Index/info', header = self._header,
                              data = data,
                              timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
        if info['code'] != 0:
            return info
        if IP in info['response']:
            return '白名单添加成功'
        else:
            return f'IP{IP},无法加入黑名单'

    @ProxyBridging
    @rh.result_handle
    def re_order(self, param):
        if not self._header['Cookie'] or self._header['Cookie'] == '':
            return {'code': Code.code(108), 'response': self._header['Cookie']}
        try:
            ids, times, urls, numbers, datas = [], [], [], [], []
            goods_type = param['platform_goods_table']['goods_type']
            url = param['url']
            number = param["number"]
            params = {
                    'style_id':  goods_type,
                    'a':         'orderlist',
                    's':         'Index',
                    'order_url': url
            }
            params = parse.urlencode(params)
            info = self.Http.get(self._platform_url + f'/index.php?{params}',
                                 header = self._header,
                                 timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if info['code'] != 0:
                return info
            html = etree.HTML(info['response'])
            tr_list = html.xpath('//table/tr')
            for tr in tr_list[1:]:
                _id = str(tr.xpath('./td[1]//text()')[0])
                _time = str(tr.xpath('./td[9]/font[1]/text()')[0])
                _url = str(tr.xpath('./td[2]/div/b/a/@href')[0])
                _number = str(tr.xpath('./td[5]/text()')[0]).split('/')[-1]
                if str(_url) == str(url) and str(_number) == str(number):
                    ids.append(_id)
                    times.append(_time)
                    urls.append(_url)
                    numbers.append(_number)
                    datas.append(tr)
            return {'code':     0, 're_id': ids, 're_url': urls, 're_time': times, 're_number': numbers,
                    're_info':  datas,
                    'response': info['response']}

        except Exception as e:
            return {'code': 102, 'msg': f'未处理异常{e}', 'response': ''}

    @ProxyBridging
    @rh.result_handle
    def collection(self, param):
        if not self._header['Cookie'] or self._header['Cookie'] == '':
            return {'code': Code.code(108), 'response': self._header['Cookie']}
        try:
            order_id = str(param['callback2'])
            data = {
                    'token':     self._key,
                    'timestamp': time.time(),
                    'order_id':  order_id,
            }
            info = self.Http.post(self._platform_url + '/index.php?s=/External/order_query', header = self._header,
                                  data = data,
                                  timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if info['code'] != 0:
                return info
            _info = info['json']
            if 'ok' in _info['message'] and _info['error_code'] == 0:
                data = _info['data'][0]
                number_ = data['order_speednum']
                start_number = ''
                order_pid = param["parameters"]['order_pid']
                if order_pid == '2':
                    start_number = data['start_pl_count']
                status = self._status.get(str(data['order_state']), '未知状态')
                start_number_data = {
                        "start_number": data.get("start_pl_count", ''),
                        "start_info":   data,
                }
                return {'code':         0, 'msg': 'success', 'number': number_, 'status': status,
                        'start_number': start_number, 'affixation': start_number_data,
                        'response':     str(data)}
            else:
                return {'code': Code.code(107), 'msg': f'订单采集失败', 'response': str(_info)}

        except Exception as e:
            return {'code': Code.code(107), 'msg': f'采集订单进度失败 {e}', 'response': f'采集订单进度失败 {e}'}

    @ProxyBridging
    @rh.result_handle
    def get_id(self, param):
        if not self._header['Cookie'] or self._header['Cookie'] == '':
            return {'code': Code.code(108), 'response': self._header['Cookie']}
        ids, times, urls, datas, numbers, batchs = [], [], [], [], [], []
        try:
            goods_type = param['platform_goods_table']['goods_type']
            info = self.Http.get(self._platform_url + f'/index.php?s=/Index/orderlist/style_id/{goods_type}',
                                 header = self._header,
                                 timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if info['code'] != 0:
                return info
            html = etree.HTML(info['response'])
            tr_list = html.xpath('//table/tr')
            for tr in tr_list[1:]:
                _id = str(tr.xpath('./td[1]//text()')[0])
                _time = str(tr.xpath('./td[9]/font[1]/text()')[0])
                _url = str(tr.xpath('./td[2]/div/b/a/@href')[0])
                _number = str(tr.xpath('./td[5]/text()')[0]).split('/')[-1]
                _start_number = str(tr.xpath('./td[4]/text()')[0])
                _order_status = str(tr.xpath('./td[8]//text()')[0])
                _order_status = self._status.get(_order_status, '未知状态')
                _callback = {
                        "goods_id":          param['goods_id'].replace('_', ','),
                        "platform_order_id": _id,
                        "number":            _number,
                        "error":             "",
                        "start_number":      _start_number,
                        "status":            _order_status,
                }
                ids.append(_id)
                numbers.append(_number)
                urls.append(_url)
                times.append(_time)
                datas.append(tr_list[1:])
                batchs.append(_callback)
            return {'code': Code.code(0), 'count': len(ids), 'ID': ids, 'TIME': times,
                    'URL':  urls, 'NUMBER': numbers, 'DATA': datas, 'BATCH': batchs}

        except Exception as e:
            return {'code': Code.code(107), 'msg': f'对比订单失败 {e}', 'response': f'对比订单失败 {e}'}

    @ProxyBridging
    @rh.result_handle
    def refund(self, param):
        if not self._header['Cookie'] or self._header['Cookie'] == '':
            return {'code': Code.code(108), 'response': self._header['Cookie']}
        try:
            info = self.collection(param)
            if info['code'] != 0:
                return info
            status = info.get('status', '')
            number = info.get('number', '')
            if str(status) in ['成功', '异常', '退款', '完成']:
                return {'code':     0, 'msg': '退款成功', 'status': status, 'number': number,
                        'response': str(info)}
            if str(status) in ["申请退款"]:
                return {'code':     106, 'msg': '退款等待中', 'status': status, 'number': number,
                        'response': str(info)}
            id_ = str(param['callback2'])
            data = {
                    'token':     self._key,
                    'timestamp': time.time(),
                    'order_id':  id_,
            }
            info = self.Http.post(self._platform_url + '/index.php?s=/External/order_refund', header = self._header,
                                  data = data,
                                  timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
            if info['code'] != 0:
                return info
            _info = info['json']
            if _info['error_code'] == 0 and '退款已经申请' in _info['message']:
                return {'code':     106, 'msg': '退款提交成功', 'status': status, 'number': number,
                        'response': str(info)}
        except Exception as e:
            return {'code': 107, 'msg': f'退款异常{e}'}

    @ProxyBridging
    @rh.result_handle
    def checkout_wallet(self, param, platform_id, wallet_type):
        if wallet_type == self.WALLET_TYPE_DEDUCTION:
            try:
                if not self._header['Cookie'] or self._header['Cookie'] == '':
                    return {'code': Code.code(108), 'response': self._header['Cookie']}
                before_price = param['deve_money']
                data = {
                        'token':     self._key,
                        'timestamp': time.time(),
                        'order_id':  platform_id,
                }
                info = self.Http.post(self._platform_url + '/index.php?s=/External/order_query', header = self._header,
                                      data = data,
                                      timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
                if info['code'] != 0:
                    return info
                _info = info['json']
                if 'ok' in _info['message'] and _info['error_code'] == 0:
                    data_ = _info['data'][0]
                    after_price = data_['order_money']
                    create_time = data_['order_timer']
                    data = {
                            'flow_id':     platform_id,
                            'balance':     '',
                            'flow_type':   wallet_type,
                            'create_time': create_time,
                            'amount':      after_price,
                            'row_data':    data_
                    }
                    if float(before_price) - abs(float(after_price)) < -0.1:
                        raise WalletError(err_data = {'after_price': after_price})
                    return {'code': Code.code(0), 'msg': 'success', 'data': data}
                else:
                    return {"code": 107, "msg": '未找到该订单'}
            except Exception as e:
                return {"code": 107, "msg": f"流水对比异常{e}"}

    @ProxyBridging
    @rh.result_handle
    def batch_collection(self, orders: dict) -> dict:
        collection_data = {}
        ids = ''
        for order in orders:
            if ids == '':
                ids = order['callback2']
            else:
                ids = f"{ids},{order['callback2']}"
            collection_data.update(
                    {
                            order['callback2']: {
                                    'order_id': order['order_id'],
                                    'url':      order['url'],
                                    'number':   order['number'],
                                    'goods_id': order['goods_id'],
                            }
                    })
        data = {
                'token':     self._key,
                'timestamp': time.time(),
                'order_id':  ids,
        }
        info = self.Http.post(self._platform_url + '/index.php?s=/External/order_query', header = self._header,
                              data = data,
                              timeout = self.REQUEST_TIMEOUT, proxies = self.PROXY)
        if info['code'] != 0:
            return info
        _info = info['json']
        if 'ok' in _info['message'] and _info['error_code'] == 0:
            for item in _info['data']:
                collection_data[str(item['order_id'])].update({'brushed': int(item['order_speednum'])})
                collection_data[str(item['order_id'])].update(
                        {'status': self._status.get(str(item['order_state']), '未知状态')})
                collection_data[str(item['order_id'])].update({'start_number': item['start_pl_count']})
                collection_data[str(item['order_id'])].update({'affixation': {
                        "start_number": item['start_pl_count'],
                }})
        return {
                'code':        0,
                'msg':         '获取成功',
                'collections': collection_data
        }


WeiPingTai = WeiPingTai()
