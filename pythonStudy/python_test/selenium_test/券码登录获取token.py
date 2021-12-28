# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 12:21
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 券码登录获取token.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
import time
from PIL import Image
from chaojiying import *
import numpy as np


class QuanMaWuYou(object):
    def __init__(self, *args, **kwargs):
        super(QuanMaWuYou, self).__init__(*args, **kwargs)
        self._header = {
                'token':        '',
                'channelid':    'C00001',
                'Content-Type': 'application/json;charset=UTF-8',
                'User-Agent':   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        }
        self._status = {
                '0': '待充',
                '1': '充值中',
                '2': '上报充值',
                '3': '关闭',
                '4': '成功',
                '5': '纠纷',
        }


    def init_driver(self, user, password):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option("prefs", {"profile.mamaged_default_content_settings.images": 2})
        self.browser = webdriver.Chrome(options = self.options)
        # size_Dict = self.browser.get_window_size()
        # # 打印浏览器的宽和高
        # print("当前浏览器的宽：", size_Dict['width'])
        # print("当前浏览器的高：", size_Dict['height'])
        self.browser.set_window_size(width = 1920, height = 1080, windowHandle = "current")
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                                                Object.defineProperty(navigator, 'webdriver', {
                                                  get: () => undefined
                                                })
                                              """
        })
        self.wait = WebDriverWait(self.browser, 100)
        self.trackList = []
        self.AC = ActionChains(self.browser)
        self._platform_url = 'http://quanma51.com'
        self.browser.maximize_window()
        self.browser.get(f'{self._platform_url}/pc/#/login')
        sleep(2)
        user_location = self.browser.find_element_by_xpath('//div[@class="login-form margin-auto"]/div[2]/div/input')
        user_location.send_keys(user)
        password_location = self.browser.find_element_by_xpath(
            '//div[@class="login-form margin-auto"]/div[3]/div/input')
        password_location.send_keys(password)
        sleep(1)
        slide = self.browser.find_element_by_id('nc_1_n1t')
        self.AC.click_and_hold(slide)
        self.AC.move_by_offset(xoffset = 350, yoffset = 0).perform()
        self.AC.pause(0.5).release().perform()
        self.browser.find_element_by_xpath('//div[@class="mt20"]/button').click()
        sleep(2)
        token = self.browser.execute_script('return localStorage.getItem("token");')
        print(token)
        return self.browser

    def run(self):
        start = time.time()
        self.init_driver(user=15710856659,password=15710856659)
        print(time.time() - start)


QuanMaWuYou = QuanMaWuYou()
if __name__ == '__main__':
    QuanMaWuYou.run()
