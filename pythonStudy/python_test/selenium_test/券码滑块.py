# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 11:02
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 券码滑块.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image

class QM(object):
    def __init__(self, *args, **kwargs):
        super(QM, self).__init__(*args, **kwargs)
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
        self.action = ActionChains(self.browser)

    def skip(self):
        self.browser.maximize_window()
        self.browser.get('http://quanma51.com/pc/#/login')
        sleep(2)
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button')))
        self.action.click_and_hold(button)
        self.action.move_by_offset(300, 0).perform()
        # for i in range(5):
        #     # .perform()表示立即执行动作链操作
        #     self.action.move_by_offset(59, 0).perform()
        #     sleep(0.5)
        sleep(10)
        if '验证通过' in self.browser.page_source:
            print('滑块验证通过')
        return self.browser

QM = QM()
if __name__ == '__main__':
    QM.skip()