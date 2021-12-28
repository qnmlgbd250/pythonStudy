# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 16:51
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 规避检测.py
# @Software: PyCharm
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get('http://exercise.kingname.info')