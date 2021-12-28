# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 12:38
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : YouTuBe爬虫.py
# @Software: PyCharm
import requests
import re
import json
from selenium import webdriver
from time import sleep
import time
from lxml import etree


class YouTuBe(object):

    def __init__(self, *args, **kwargs):
        super(YouTuBe, self).__init__(*args, **kwargs)

    def you(self):
        res = requests.get('https://www.youtube.com/channel/UCDBOF3D9DTVSJgq7J7V3aTw/videos')
        ytInitialData = re.findall(r'var ytInitialData = (.*?);</script>', res.text)
        contents = json.loads(ytInitialData[0])
        items = contents['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content'][
            'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']
        items = items[:-1]
        for item in items:
            videoid = item['gridVideoRenderer']['videoId']
            print(videoid)

    def youpro(self):
        data = '{"context":{"client":{"hl":"zh-CN","gl":"JP","remoteHost":"8.37.43.208","deviceMake":"","deviceModel":"","visitorData":"CgtoQldiVlZKVDl5USiYvc2IBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20210810.01.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/channel/UCDBOF3D9DTVSJgq7J7V3aTw/videos","screenPixelDensity":2,"platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","screenDensityFloat":1.5,"timeZone":"Asia/Shanghai","browserName":"Chrome","browserVersion":"92.0.4515.107","screenWidthPoints":1494,"screenHeightPoints":225,"utcOffsetMinutes":480,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/channel/UCDBOF3D9DTVSJgq7J7V3aTw/videos","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clickTracking":{"clickTrackingParams":"CAAQhGciEwiG3KygnajyAhVHxEwCHZNLDzY="},"adSignalsInfo":{"params":[{"key":"dt","value":"1628659352969"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"480"},{"key":"u_his","value":"7"},{"key":"u_java","value":"false"},{"key":"u_h","value":"934"},{"key":"u_w","value":"1494"},{"key":"u_ah","value":"894"},{"key":"u_aw","value":"1494"},{"key":"u_cd","value":"24"},{"key":"u_nplug","value":"3"},{"key":"u_nmime","value":"4"},{"key":"bc","value":"31"},{"key":"bih","value":"225"},{"key":"biw","value":"1478"},{"key":"brdim","value":"0,0,0,0,1494,0,1494,894,1494,225"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"continuation":"4qmFsgKPARIYVUNEQk9GM0Q5RFRWU0pncTdKN1YzYVR3GkRFZ1oyYVdSbGIzTVlBeUFBTUFFNEFlb0RHME5uVGtSU1JXdFRRM2RxVjJwaE5uUmZTWEpOZDNZNFFrdEVTUSUzRCUzRJoCLGJyb3dzZS1mZWVkVUNEQk9GM0Q5RFRWU0pncTdKN1YzYVR3dmlkZW9zMTAy"}'
        res = requests.post('https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
                            data = data)
        print(res.text)


class YouTuBeplus(object):

    def __init__(self, *args, **kwargs):
        super(YouTuBeplus, self).__init__(*args, **kwargs)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options = self.options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                                Object.defineProperty(navigator, 'webdriver', {
                                  get: () => undefined
                                })
                              """
        })
        self.url_list = ['https://www.youtube.com/watch?v=G01wzhPrzuo']
        self.dowm_turn_url = 'https://yt1s.com/api/ajaxSearch/index'
        self.covert_url = 'https://yt1s.com/api/ajaxConvert/convert'
        self.anchor_page_url = 'https://www.youtube.com/channel/UCDBOF3D9DTVSJgq7J7V3aTw/videos'

    def get_page_souse(self):
        self.driver.get(self.anchor_page_url)
        count = 0
        while count < 8:
            self.driver.execute_script(f'window.scrollTo({count * 500},{(count + 1) * 500})')
            sleep(1)
            count += 1
        return self.driver.page_source

    def resolve_page(self):
        tree = etree.HTML(self.get_page_souse())
        items = tree.xpath('//*[@id="items"]/ytd-grid-video-renderer')
        for item in items:
            href = item.xpath('.//@href')
            url = 'https://www.youtube.com' + href[0]
            self.url_list.append(url)
    def get_convert_link(self):
        self.resolve_page()
        self.url_list = list(set(self.url_list))
        for url_ in self.url_list:
            data = {
                'q': url_,
                'vt': 'home'
            }
            res_ = requests.post(self.dowm_turn_url,data = data)
            info = json.loads(res_.text)
            mp4_size = info['links']['mp4']
            vid = info['vid']
            k = ''
            if '135' in str(mp4_size):      # 480p
                k = mp4_size['135']['k']
            if '22' in str(mp4_size):       # 720p
                k = mp4_size['22']['k']
            elif '299' in str(mp4_size):    # 1080p
                k = mp4_size['299']['k']
            if k == '':
                print('分辨率太低,跳过下载')
                continue
            data_ = {
                'vid': vid,
                'k': k
            }
            resp_ = requests.post(self.covert_url, data = data_)
            info_ = json.loads(resp_.text)
            if info_['status'] == 'ok':
                dlink = info_['dlink']
                print(dlink)





YouTuBe = YouTuBe()
YouTuBeplus = YouTuBeplus()
if __name__ == '__main__':
    # YouTuBe.you()
    # YouTuBe.youpro()
    YouTuBeplus.get_convert_link()
