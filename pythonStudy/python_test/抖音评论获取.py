# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 11:06
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 抖音评论获取.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time    : 2021/11/17 15:09
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 抖音评论获取.py
# @Software: PyCharm

import requests
import re

headers = {
# 'cookie': 'ttwid=1%7CTmEwKq4CJs3Qqw17w2AWb2Ux6YqIU1fDZrOAkEpKCjo%7C1630483173%7C06d523e4d59554a4762748917355f6b1b1ff1df8e8d3683ea2422bd1cea26ce6; MONITOR_WEB_ID=7a84dc1a-5424-4d97-b193-e12577ac2972; ttcid=79ddf7d84203476c808c9e360825103536; passport_csrf_token_default=b37dfbc899ad2ebffd824a093e49a112; passport_csrf_token=b37dfbc899ad2ebffd824a093e49a112; _tea_utm_cache_6383=undefined; _tea_utm_cache_1300=undefined; s_v_web_id=verify_kw1g23px_dlCbFEbN_Q1Y6_4M3U_9Dpj_woMGR98S8iVE; _tea_utm_cache_2018=undefined; odin_tt=3c3238d43366559974fd4c1c53441dcca56e2964aa98688f342ebaff827874433a48a7a3ede10775c5848137e59fb9e560bab1ef8ef376605b9d9cc729ed4982; msToken=8ti4Z8dpk5V_S_ETu6TqCSAbyMdDM6a-WTMsltILPCuuIX5QYpn7ykVowQHL4U4oHMB7TAWC6qLHVG_fcMrLWVzoFch0wN7x5S-FnwFa1qBwHQpD5B6na8g=; MONITOR_DEVICE_ID=f6f9fadf-4615-4548-912f-b97f2581eaa5; douyin.com; __ac_signature=_02B4Z6wo00f01ToSVrgAAIDBuhCs-COuoyk6NlIAAC8TzVQMT9Y90w4Szn2j6-dze57vqmWqLSgT75dw3ajKpaUPApRN09ued0hEzFFaUbR9L0eCUL7Pxoj3lxihcTqgkM3kS0GbXCFQ60v82d; tt_scid=xC2SOX1lfc3yff4w2D28AUa6dlDNj3Sv5-tqEz.4THpYTqiNlw9hdaiipIE4stc8a056; msToken=4vx6FxNP5MoQu1mF6UyoLGmAuobKS26sObKiR4s-9w_10cys25XSqUpi-_pCpLlk8TgON6WpRdZrnb4gzdlUVoN74QO-hfv4uuEv4QH3CSD-9M6v7agCcrty',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'

}

url = 'https://www.douyin.com/video/7031330242799095075?previous_page=app_code_link'
api_url = 'https://aweme-hl.snssdk.com/aweme/v1/aweme/detail/?aweme_id=7031330242799095075&device_platform=ios&app_name=aweme&aid=1128'
comment_url = 'https://www.douyin.com/aweme/v2/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7031093277017394470&cursor=0&count=10000'



reply_url = 'https://www.douyin.com/aweme/v2/web/comment/list/reply/?device_platform=webapp&aid=6383&channel=channel_pc_web&item_id=7031093277017394470&comment_id=7031093659961754382&cursor=13&count=100&cookie_enabled=true'

u111 = 'https://www.douyin.com/aweme/v2/web/comment/list/reply/?device_platform=webapp&aid=6383&channel=channel_pc_web&item_id=7018480511412653323&comment_id=7018485260271158024&cursor=0&count=10&cookie_enabled=true'

'https://www.douyin.com/aweme/v1/web/comment/list/reply/?device_platform=webapp&aid=6383&channel=channel_pc_web&item_id=7031093277017394470&comment_id=7031093659961754382&cursor=43&count=10&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2066&screen_height=1162&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F95.0.4638.69+Safari%2F537.36+Edg%2F95.0.1020.44&browser_online=true&msToken=Q_OqhW49E-0E8RQxjjTN4IHoMOUe9rUyQ9Z_4iArViBuM2Pu5Oo3nUg1msVo8fufkRWOHmJY6BtjkLrisqUQ0B8NDBIdThQ5L3CTMgM2GC054mGM-4ubPQm1PQ==&X-Bogus=DFSzsdVuDX0ANSfJS7D2Yl9WX7rW&_signature=_02B4Z6wo00001qMzu6gAAIDCIzFB60opKeajN78AAMlkxQLgbrbrCy4pW-RwUwazcsCl1gs1Y5tVkn6sV08WDmd-RtihQk3e1yvqItNL83BoQNG3D4ASgHfCwicWYvRakZq2evLW6ljI-.976c'
comments = requests.get(u111, headers = headers)
# comments.encoding = comments.apparent_encoding
print(comments.text)
