# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 9:01
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 商品爬虫.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import time
from lxml import etree
import requests


class Alibaba(object):
    def __init__(self, **kwargs):
        super(Alibaba, self).__init__()
        self._url = input('请输入1688商品链接: ')
        # self._url = 'https://detail.1688.com/offer/652896058216.html?spm=a26352.b28411319.offerlist.158.4da51e62OpRh9i'
        self.browser = None

    def ini_browser(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        browser = webdriver.Chrome(options = options)
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                                Object.defineProperty(navigator, 'webdriver', {
                                  get: () => undefined
                                })
                              """
        })
        self.browser = browser




    def time_end(self, second = 10):
        count = 0
        while (count < second):
            count_now = second - count
            print("\r", f'倒计时还有{count_now}秒', flush = True, end = "", )
            time.sleep(1)
            count += 1

    def skip(self):
        self.ini_browser()
        self.browser.get(self._url)
        if '验证' in self.browser.title:
            print('出现安全验证...')
            sleep(2)
            shuaxin = True
            while shuaxin:
                sleep(2)
                button = self.browser.find_element_by_id('nc_1_n1z')
                ActionChains(self.browser).click_and_hold(button).move_by_offset(300, 0).perform()
                if '刷新' not in self.browser.page_source:
                    shuaxin = False
                else:
                    sleep(2)
                    knob = self.browser.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/center/div[1]/div/span/a")
                    ActionChains(self.browser).click(knob).perform()
                    continue

        print('安全验证完成...')
        try:
            login_x = self.browser.find_element_by_xpath('/html/body/div[8]/div[2]/div')
            ActionChains(self.browser).click(login_x).perform()
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(2)
            return self.browser.page_source
        except:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(2)
            return self.browser.page_source

    def get_jpg(self):
        page_source = self.skip()
        html = etree.HTML(page_source)
        main_jpg_list = html.xpath('//*[@id="mod-detail-bd"]/div[1]/div[2]/div/div/div/@data-gallery-image-list')
        if main_jpg_list == []:
            main_jpg_list_ = html.xpath('/html/body/div[1]/div[4]/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div/div/div[2]/div/ul/li//@data-imgs')
            main_jpg_list_ += html.xpath(
            '/html/body/div[1]/div[4]/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div/div/div[2]/div/ul/@data-imgs')
            for main_png in main_jpg_list_:
                main_jpg_list.append(json.loads(str(main_png))['preview'])
        else:
            main_jpg_list = list(main_jpg_list)[0].split(',')

        detail_jpg_src_list = []
        detail_jpg_list = html.xpath('/html/body/div[1]/div[2]/div[3]/div/div/div/div[5]/div/div/div/div[1]/div/p/img')

        if detail_jpg_list == []:
            detail_jpg_list = html.xpath('/html/body/div[1]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[7]/div/div/div/div[1]/div/p[3]/img')
            detail_jpg_list += html.xpath(
                '/html/body/div[1]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[7]/div/div/div/div[1]/div/p[2]/img')
            detail_jpg_list += html.xpath('/html/body/div[1]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[7]/div/div/div/div[1]/div/p/span[2]/strong/img')
            detail_jpg_list += html.xpath(
            '/html/body/div[1]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[7]/div/div/div/div[1]/div/p/img')


        for img in detail_jpg_list:
            src = img.xpath('./@src')[0]
            detail_jpg_src_list.append(src)

        return main_jpg_list, detail_jpg_src_list

    def sove_jpg(self):
        import os
        main_jpg_list, detail_jpg_src_list = self.get_jpg()
        main_jpg_list = [i for i in main_jpg_list if i != ' ' or '']
        for main_img in main_jpg_list:
            r = requests.get(main_img.strip())
            main_name = main_img.split('/')[-1]
            for_name = re.findall(r'(\d+).html', self._url)[0]
            main_path = f'./{for_name}主图/'
            if not os.path.exists(main_path):
                os.makedirs(main_path)
            with open(main_path + main_name, 'wb') as f:
                f.write(r.content)
                print(f'图片{main_img}下载完成')

        detail_jpg_src_list = [i for i in detail_jpg_src_list if i != ' ' or '']
        for detail_jpg in detail_jpg_src_list:
            r = requests.get(detail_jpg.strip())
            main_name = detail_jpg.split('/')[-1]
            for_name = re.findall(r'(\d+).html', self._url)[0]
            main_path = f'./{for_name}详情图/'
            if not os.path.exists(main_path):
                os.makedirs(main_path)
            with open(main_path + main_name, 'wb') as f:
                f.write(r.content)
                print(f'图片{detail_jpg}下载完成')
        self.browser.quit()


Alibaba = Alibaba()
if __name__ == '__main__':
    Alibaba.sove_jpg()
