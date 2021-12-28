# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 18:42
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 微信开始数脚本.py
# @Software: PyCharm
import requests
import re

def get_wx_name(url):
    try:
        headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                              "like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c31) NetType/WIFI "
                              "Language/zh_CN",
        }

        info = requests.get(url, headers = headers, timeout = 5)
        if '参数错误' in info.text:
            return False
        content_list = re.findall(r"var msg_title = '(.*?)'\.html", info.text, re.S)
        nickname = re.findall(r'var nickname = "(.*?)";', info.text, re.S)
        if len(nickname) != 0:
            nickname = nickname[0]
        else:
            nickname = re.findall(r"window\.nickname = '(.*?)'", info.text, re.S)
            if len(nickname) != 0:
                nickname = nickname[0]
            else:
                re_str = r"d\.nick_name = xml \? getXmlValue\('nick_name\.DATA'\) : '(.*?)';"
                nickname = re.findall(re_str, info.text, re.S)
                if nickname:
                    nickname = nickname[0]
                else:
                    nickname = ''
        mid = re.findall(r'var user_name = "([\S.]+)"', info.text)
        if content_list:
            content_title = content_list[0]
        else:
            content_list = re.findall(r"window.msg_title = '(.*?)'", info.text, re.S)
            if len(content_list) != 0:
                content_title = content_list[0]
            else:
                re_str = r"d\.title = xml \? getXmlValue\('title\.DATA'\) : '(.*?)';"
                content_list = re.findall(re_str, info.text, re.S)
                if content_list:
                    content_title = content_list[0]
                else:
                    content_title = ''
        mid = re.findall(r'var user_name = "([\S.]+)"', info.text)
        if len(mid) != 0:
            mid = mid[0]
        else:
            re_str = r"d.user_name = getXmlValue\('user_name.DATA'\) \|\| '(.*?)';"
            mid = re.findall(re_str, info.text, re.S)
            if not mid:
                re_str = r"d\.user_name = xml \? getXmlValue\('user_name\.DATA'\) : '(.*?)';"
                mid = re.findall(re_str, info.text, re.S)
            mid = mid[0]
        content = re.findall(r'var msg_desc = "(.*?)"', info.text, re.S)
        if content:
            content = content[0]
        else:
            content = re.findall(r"window.msg_desc = '(.*?)'", info.text, re.S)
            if len(content) != 0:
                content = content[0]
            else:
                content = ''

        user_name = re.findall(r'profile_meta_value\">([a-zA-Z][-_a-zA-Z0-9]{5,19})</', info.text)

        if len(user_name) <= 0:
            user_name = ['']

        if mid and content_title:
            _res = {
                    'code':          0,
                    'mid':           mid,  # 微信原始id
                    'user_name':     user_name[0],  # 微信公众号名称
                    'content':       content,  # 文章内容
                    'content_title': content_title,  # 标题
                    'nickname':      nickname  # 用户昵称
            }
            return _res
        else:
            return False

    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        print(get_wx_name('https://mp.weixin.qq.com/s/5Brw0f5INP724fEcD50h7g'))