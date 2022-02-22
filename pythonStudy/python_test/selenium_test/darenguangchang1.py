# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 15:13
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : darenguangchang1.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import re
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
from lxml import etree
import requests
from selenium.webdriver.support.ui import WebDriverWait


class DOU(object):
    def __init__(self, **kwargs):
        super(DOU, self).__init__()
        self.api_url = 'https://fxg.jinritemai.com/login?from=buyin'

    def get_cookie_PDD(self):
        """
        登录账号
        Returns:

        """
        try:
            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 100)
            driver.maximize_window()
            driver.get(self.api_url)
            sleep(2)
            # 切换验证码登录形式
            bowton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'account-center-qrcode-switch-action')))
            bowton.click()
            sleep(3)
            # 输入手机号
            phone_number = '13934305054'
            driver.find_element(By.XPATH,'//*[@id="sdk-login-box"]/section/div[4]/div[1]/div[2]/div/input').send_keys(phone_number)
            sleep(60)
            if '登录' in driver.title:
                print('登录失败')
                driver.quit()
            else:
                print("登录成功")
                sleep(2)
                dictCookies = driver.get_cookies()  # 获取list的cookies
                jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
                with open('抖店_cookies.txt', 'w') as f:
                    f.write(jsonCookies)
                print('cookies保存成功！')
                driver.quit()
        except Exception as e:
            print(f"登录出错 => {e}")

    def browser_initial(self):
        """
        初始化浏览器
        Returns:

        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 规避检测
        browser = webdriver.Chrome(options = options)
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
        })
        browser.maximize_window()
        browser.get('https://fxg.jinritemai.com/')
        return browser

    def login_DOU(self, browser):
        try:
            with open('抖店_cookies.txt', 'r', encoding = 'utf8') as f:
                listCookies = json.loads(f.read())
        except:
            print('关闭当前窗口,登录获取cookie...')
            browser.quit()
            # 往browser里添加cookies
        for cookie in listCookies:
            cookie_dict = {
                'domain': 'fxg.jinritemai.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": '',
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            browser.add_cookie(cookie_dict)
        browser.refresh()  # 刷新网页,cookies才成功
        if '登录' in browser.title:
            print('cookie可能失效,请检查cookie是否在有效期内...')
            browser.quit()
            self.get_cookie_PDD()
            browser = 'cookie可能失效,请检查cookie是否在有效期内...'
        print('成功')
        return browser

    def spider_DOU(self,browser):
        browser.get('https://buyin.jinritemai.com/dashboard/servicehall/daren-square?previous_page_name=3')
        sleep(2)
        while '抖音电商官网-抖音小店入驻-兴趣电商直播带货平台' in browser.title:
            browser.get('https://buyin.jinritemai.com/dashboard/servicehall/daren-square?previous_page_name=3')
            print('测试')
        if '巨量百应Buyin' in browser.title:
            print('点击进入商家后台')
        sleep(1000)



DOU = DOU()
if __name__ == '__main__':
    DOU.spider_DOU(DOU.login_DOU(DOU.browser_initial()))