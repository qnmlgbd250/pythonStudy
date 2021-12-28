# -*- coding: utf-8 -*-
# @Time    : 2021/12/24 15:46
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 小红书爬虫.py
# @Software: PyCharm
import requests
import re
from urllib.parse import unquote, parse_qs

headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 '
                      'MQQBrowser/8.9 Mobile Safari/537.36',

}
data = {
        "id":   "86ad5c364892ff66ab4363dea0c304d3",
        "sign": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62~~~false~~~zh-CN~~~24~~~8~~~8~~~-480~~~Asia/Shanghai~~~1~~~1~~~1~~~1~~~unknown~~~Win32~~~Microsoft Edge PDF Plugin::Portable Document Format::application/x-google-chrome-pdf~pdf,Microsoft Edge PDF Viewer::::application/pdf~pdf,Native Client::::application/x-nacl~,application/x-pnacl~~~~canvas winding:yes~canvas fp:c50d17e4ba86b8c848e9b3ead86ad4a8~~~false~~~false~~~false~~~false~~~false~~~0;false;false~~~4;7;8~~~124.04347527516074"
}
resp = requests.post('https://www.xiaohongshu.com/fe_api/burdock/v2/shield/registerCanvas?p=cc', headers = headers, data = data)
print(resp.text)
