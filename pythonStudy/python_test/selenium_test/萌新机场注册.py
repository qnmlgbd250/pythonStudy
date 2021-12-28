# -*- coding: utf-8 -*-
# @Time    : 2021/8/8 9:18
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 萌新机场注册.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from PIL import Image
from chaojiying import *
import numpy as np


class Mengxin(object):

    def __init__(self, *args, **kwargs):
        super(Mengxin, self).__init__(*args, **kwargs)
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options = self.options)
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
        # self.options.add_argument('window-size=1920x1080')

    def init_driver(self):
        self.browser.maximize_window()
        self.browser.get('https://www.mxyssr.cc/auth/register')
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_radar_tip'))).click()
        sleep(3)
        return self.browser

    def __del(self):
        sleep(2)
        self.browser.close()

    def skip(self):
        self.init_driver()
        self.get_distance()
        self.distinguish()
        self.get_tracks(self.distance,1,'ease_out_expo')
        print(self.trackList)
        print(self.distance)
        block = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        while True:
            count = 0
            self.AC.click_and_hold(block).perform()
            for track in self.trackList:
                self.AC.move_by_offset(track, 0).perform()
                print('移动距离',track)
                count += 1
                print('滑动次数',count)
            self.AC.pause(0.5).release().perform()

    def get_trackList(self, distance = 20, f_rate = 0.5, m_rate = 0.3, t = 0.2, v = 0):
        # 加速减速的临界值
        f = f_rate * distance
        m = m_rate * distance
        # 当前位移
        s = 0
        # 循环
        while s < distance:
            # 初始速度
            v0 = v
            if s < f:
                a = 20
            elif s < f + m:
                a = 0
            else:
                a = -3
            # 计算当前t时间段走的距离
            s0 = v0 * t + 0.5 * a * t * t
            # 计算当前速度
            v = v0 + a * t
            # 四舍五入距离，因为像素没有小数
            self.trackList.append(round(s0))
            # 计算当前距离
            s += s0
        print(self.trackList)

    def get_distance(self):
        self.browser.save_screenshot('aa.png')
        code_img_ele = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
        location = code_img_ele.location  # 验证码图片左上角的坐标 x,y
        print('location:', location)
        size = code_img_ele.size  # 验证码标签对应的长和宽
        print('size:', size)
        rangle = (
            int(location['x']), int(location['y']), int(location['x'] + size['width'] ),
            int(location['y'] + size['height']))
        # 至此验证码图片区域就确定下来了
        print(rangle)
        i = Image.open('./aa.png')
        code_img_name = './code.png'
        # i = i.resize((258,159))
        # crop根据指定区域进行图片裁剪
        frame = i.crop(rangle)
        frame.save(code_img_name)

    def distinguish(self):
        """
        超级鹰解析验证码
        :return:
        """
        self.distance = ''
        _chaojiying = Chaojiying_Client('17633935269', '12345678', '909647')  # 用户中心>>软件ID 生成一个替换 96001
        im = open('code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        _chaojiying_res = _chaojiying.PostPic(im, 9101)
        print(_chaojiying_res)
        x_at = _chaojiying_res['pic_str']
        x_at = x_at.split(',')[0]
        print('x坐标:',x_at)
        self.distance = float(x_at) *0.8

    def get_tracks(self,distance, seconds, ease_func):
        tracks = [0]
        offsets = [0]
        for t in np.arange(0.0, seconds, 0.1):
            ease = globals()[ease_func]
            offset = round(ease(t / seconds) * distance)
            self.trackList.append(offset - offsets[-1])
            offsets.append(offset)

def ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)

Mengxin = Mengxin()
if __name__ == '__main__':
    Mengxin.skip()
