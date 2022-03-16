# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 10:15
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 豆瓣滑块验证码.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class DouBan(object):
    def __init__(self, *args, **kwargs):
        super(DouBan, self).__init__(*args, **kwargs)

    def init_driver(self):
        options = webdriver.ChromeOptions()
        service = Service('chromedriver.exe')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options = options, service = service)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

        # script = '''
        # Object.defineProperty(navigator, 'webdriver', {
        #     get: () => undefined
        # })
        # '''
        # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
        # # 在控制台中验证window.navigator.webdriver的值为undefined。

        return driver

    def login_web_page(self, driver):
        driver.get('https://www.douban.com/')
        action = ActionChains(driver)
        # wait = WebDriverWait(driver, 100)
        # iframe = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/iframe')
        driver.switch_to.frame(0)
        driver.find_element(By.CLASS_NAME, 'account-tab-account').click()
        driver.find_element(By.ID, 'username').send_keys(17633935268)
        driver.find_element(By.ID, 'password').send_keys(123456)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
        time.sleep(5)
        # if '拖动下方滑块完成拼图' in driver.page_source:
        driver.switch_to.frame(1)
        skip_btn = driver.find_element(By.XPATH, '//*[@id="tcaptcha_drag_thumb"]')
        action.click_and_hold(on_element = skip_btn).perform()
        action.move_to_element_with_offset(to_element = skip_btn, xoffset = 140, yoffset = 0).perform()
        tracks = self.get_tracks(distance = 64)
        print(tracks)
        for track in tracks:
            action.move_by_offset(xoffset = track, yoffset = 0).perform()
        action.release().perform()

    def get_tracks(self, distance, t = 0.3, v = 0):
        tracks = []
        mid = distance*4/5
        current = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            s = v0 * t + 0.5 * a * t * t
            current += s
            tracks.append(round(s))
            v = v0 + a * t

        return tracks




if __name__ == '__main__':
    DouBan = DouBan()
    driver_ = DouBan.init_driver()
    DouBan.login_web_page(driver_)
