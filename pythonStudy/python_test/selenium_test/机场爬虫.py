# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 20:33
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 机场爬虫.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image
from io import BytesIO
import re
from bs4 import BeautifulSoup

class jichang(object):

    def __init__(self, *args, **kwargs):
        super(jichang, self).__init__(*args, **kwargs)
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


    def init_driver(self):
        self.browser.maximize_window()
        self.browser.get('https://www.mxyssr.cc/auth/register')
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_radar_tip'))).click()
        sleep(20)
        return self.browser

    def __del__(self):
        sleep(2)
        self.browser.close()

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.browser.find_element_by_class_name("geetest_canvas_bg geetest_absolute")
        sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_image(self, name = 'captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    # def get_images(self, bg_filename = 'bg.jpg', fullbg_filename = 'fullbg.jpg'):
    #     """
    #     获取验证码图片
    #     :return: 图片的location信息
    #     """
    #     bg = []
    #     fullgb = []
    #     while bg == [] and fullgb == []:
    #         bf = BeautifulSoup(self.browser.page_source, 'lxml')
    #         bg = bf.find_all('div', class_ = 'gt_cut_bg_slice')
    #         fullgb = bf.find_all('div', class_ = 'gt_cut_fullbg_slice')
    #     bg_url = re.findall('url\(\"(.*)\"\);', bg[0].get('style'))[0].replace('webp', 'jpg')
    #     fullgb_url = re.findall('url\(\"(.*)\"\);', fullgb[0].get('style'))[0].replace('webp', 'jpg')
    #     bg_location_list = []
    #     fullbg_location_list = []
    #     for each_bg in bg:
    #         location = {}
    #         location['x'] = int(re.findall('background-position: (.*)px (.*)px;', each_bg.get('style'))[0][0])
    #         location['y'] = int(re.findall('background-position: (.*)px (.*)px;', each_bg.get('style'))[0][1])
    #         bg_location_list.append(location)
    #     for each_fullgb in fullgb:
    #         location = {}
    #         location['x'] = int(re.findall('background-position: (.*)px (.*)px;', each_fullgb.get('style'))[0][0])
    #         location['y'] = int(re.findall('background-position: (.*)px (.*)px;', each_fullgb.get('style'))[0][1])
    #         fullbg_location_list.append(location)
    #     urlretrieve(url = bg_url, filename = bg_filename)
    #     print('缺口图片下载完成')
    #     urlretrieve(url = fullgb_url, filename = fullbg_filename)
    #     print('背景图片下载完成')
    #     return bg_location_list, fullbg_location_list




if __name__ == '__main__':
    jichang().init_driver()
    jichang().get_image()