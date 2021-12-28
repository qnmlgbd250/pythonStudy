# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 16:18
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : PDD_collection.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import re
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
from lxml import etree
import requests


class PDD(object):
    def __init__(self, **kwargs):
        super(PDD, self).__init__()
        self.api_url = 'http://shop_collection.cn'

    def get_cookie_PDD(self):
        """
        登录账号
        Returns:

        """
        try:
            driver = webdriver.Chrome(executable_path = './chromedriver.exe')
            driver.maximize_window()
            driver.get('http://mobile.pinduoduo.com/login.html?')
            sleep(2)
            driver.find_element_by_xpath('//*[@id="first"]/div[2]/div').click()
            sleep(3)
            phone_number = input('输入手机号码: ')
            driver.find_element_by_xpath('//*[@id="user-mobile"]').send_keys(phone_number)
            sleep(1)
            driver.find_element_by_xpath('//*[@id="code-button"]').click()
            code = input('输入短信验证码: ')
            driver.find_element_by_xpath('//*[@id="input-code"]').send_keys(code)
            self.time_end(2)
            driver.find_element_by_xpath('//*[@id="submit-button"]').click()
            sleep(3)
            if '登录' in driver.title:
                print('登录失败')
                driver.quit()
            else:
                print("登录成功")
                sleep(2)
                dictCookies = driver.get_cookies()  # 获取list的cookies
                jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
                with open('拼多多_cookies.txt', 'w') as f:
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
        browser.get('http://mobile.pinduoduo.com/')
        return browser

    def login_PDD(self, browser):
        """
        携带cookie登录
        Args:
            browser:

        Returns:

        """
        try:
            with open('拼多多_cookies.txt', 'r', encoding = 'utf8') as f:
                listCookies = json.loads(f.read())
        except:
            print('关闭当前窗口,登录获取cookie...')
            browser.quit()

        # 往browser里添加cookies
        for cookie in listCookies:
            cookie_dict = {
                    'domain':   'mobile.pinduoduo.com',
                    'name':     cookie.get('name'),
                    'value':    cookie.get('value'),
                    "expires":  '',
                    'path':     '/',
                    'httpOnly': False,
                    'HostOnly': False,
                    'Secure':   False
            }
            browser.add_cookie(cookie_dict)
        browser.refresh()  # 刷新网页,cookies才成功
        if '登录' in browser.title:
            print('cookie可能失效,请检查cookie是否在有效期内...')
            browser.quit()
            self.get_cookie_PDD()
            browser = 'cookie可能失效,请检查cookie是否在有效期内...'
        return browser

    def spider_PDD(self, driver):
        """
        搜索商品 获取数据
        Args:
            driver:

        Returns:

        """
        sleep(2)
        if '验证' in driver.title:
            print('出现安全验证...')
            self.time_end(40)
            print('安全验证完成...')
        sleep(2)
        print('点击搜索框...')
        driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div/div/div').click()
        sleep(2)
        print('输入搜索内容...')
        search_key = input('请键入搜索词: ')
        driver.find_element_by_xpath('//*[@id="submit"]/input').send_keys(search_key)
        sleep(2)
        print('点击搜索...')
        driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div/div[2]').click()
        sleep(2)
        if '验证' in driver.title:
            print('出现安全验证...')
            self.time_end(40)
            print('安全验证完成...')
        print('请进行商品属性筛选...')
        print('倒计时30秒')
        self.time_end(30)
        count = 0
        while count < 1:
            count += 1
            if '验证' in driver.title:
                print('出现安全验证...')
                self.time_end(40)
                print('安全验证完成...')
                count = 0
            print('下拉翻页...')
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            print('翻页完成...')
            sleep(2)
        html_page = driver.page_source
        tree = etree.HTML(html_page)
        div_list = tree.xpath('//*[@class="_2EdaAb7m"]/div')
        print(len(div_list))
        shop_list = []
        title_counts = []
        title_count = 0
        for div in div_list:
            title_ = str(div.xpath('.//text()')[0])
            if 'ad' in str(title_count):
                title_count = title_count.replace('ad', '')
                title_count = int(title_count)
            if '拼了都说好' in title_:
                title_count = int(title_count)
                title_count += 1
                title_count = str(title_count) + 'ad'
                continue
            if '试试搜这些' in title_:
                title_count = int(title_count)
                title_count += 1
                title_count = str(title_count) + 'ad'
                continue
            if '相关搜索' in title_:
                title_count = int(title_count)
                title_count += 1
                title_count = str(title_count) + 'ad'
                continue
            if '品牌折扣' in title_:
                title_count = int(title_count)
                title_count += 1
                title_count = str(title_count) + 'ad'
                continue
            if '包装方式' in title_:
                title_count = int(title_count)
                title_count += 1
                title_count = str(title_count) + 'ad'
                continue
            if '查看更多' in title_:
                title_count = int(title_count)
                title_count += 1
                title_count = str(title_count) + 'ad'
                continue
            else:
                title_count = int(title_count)
                title_count += 1
                title_count = str(title_count)
                title_counts.append(title_count)
                shop_list.append(title_)
        print(len(shop_list))
        print(title_counts)

        for i in title_counts:
            print(f'爬取第{i}个商品')
            sleep(2)
            if '验证' in driver.title:
                print('出现安全验证...')
                self.time_end(40)
                print('安全验证完成...')
            if '登录' in driver.title:
                print('cookie可能失效,请检查cookie是否在有效期内...')
                driver.quit()
                self.get_cookie_PDD()
            try:
                sleep(1)
                driver.find_element_by_xpath(f'//*[@id="main"]/div/div[2]/div/div[4]/div[1]/div/div[{i}]/div').click()
            except BaseException:
                try:
                    sleep(1)
                    driver.find_element_by_xpath(
                            f'//*[@id="main"]/div/div[2]/div/div[3]/div[1]/div/div[{i}]/div').click()
                except BaseException:
                    try:
                        sleep(1)
                        driver.find_element_by_xpath(
                                f'//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[{i}]/div').click()
                    except BaseException:
                        print('标签定位错误 请联系管理员处理...')
                        # driver.back()
                        continue
            sleep(2)
            html_page = driver.page_source
            json_data = re.findall(r'window.rawData=(.*?)}};', html_page)
            try:
                json_data = json_data[0] + '}}'
                json_data = json.loads(json_data)
            except Exception as _error:
                print("没有搜索到商品json数据", _error)
                continue

            goods_url = 'http://mobile.pinduoduo.com/goods.html?goods_id=' + str(
                    json_data['store']['initDataObj']['goods']['goodsID'])

            images_list = []
            for detailGallery in json_data['store']['initDataObj']['goods']['detailGallery']:
                images_list.append(detailGallery['url'].replace('u002F', ''))

            small_images_list = []
            for viewImageData in json_data['store']['initDataObj']['goods']['viewImageData']:
                small_images_list.append(viewImageData.replace('u002F', ''))

            Product_details_list = []
            date = ''
            goodsProperty_ = {}
            for goodsProperty in json_data['store']['initDataObj']['goods']['goodsProperty']:
                if goodsProperty['key'] == '生产日期':
                    date += goodsProperty['values'][0]
                goodsProperty_[goodsProperty['key']] = str(goodsProperty['values'][0])

            skus_list = []
            for skus in json_data['store']['initDataObj']['goods']['skus']:
                skus_ = {}
                try:
                    skus_['name'] = skus['specs'][0].get('spec_value', None)
                except:
                    skus_['name'] = json_data['store']['initDataObj']['goods']['goodsName']
                skus_['price'] = skus['groupPrice']
                skus_['id'] = str(skus['skuId'])
                skus_['priceTitle'] = '拼团价'
                skus_list.append(skus_)

            video_url = ''
            if len(json_data['store']['initDataObj']['goods']['videoGallery']) != 0:
                video_url = json_data['store']['initDataObj']['goods']['videoGallery'][0]['url'].replace(
                        'u002F', '')
            shop_url = 'http://mobile.pinduoduo.com/' + json_data['store']['initDataObj']['mall']['pddRoute']
            shop_name = json_data['store']['initDataObj']['mall']['mallName']
            goods_id = json_data['store']['initDataObj']['goods']['goodsID']
            sales = json_data['store']['initDataObj']['goods']['sideSalesTip']
            if sales == '':
                sales = '已拼0件'
            title = json_data['store']['initDataObj']['goods']['goodsName']
            param = {
                    "skus":             skus_list,  # 商品参数信息
                    'images':           images_list,  # 详情图列表
                    'title':            title,  # 商品标题
                    'url':              goods_url,  # 商品链接
                    'product_details':  goodsProperty_,  # 商品描述
                    'date':             date,  # 生产日期
                    'video_url':        video_url,  # 视频介绍
                    'small_image':      small_images_list,  # 预览大图
                    'shop_url':         shop_url,  # 店铺地址
                    'shop_name':        shop_name,  # 店铺名称
                    'goods_id':         goods_id,  # 商品id
                    'describe_picture': images_list,  # 描述图片
                    'sales':            sales  # 销量
            }
            print(param)
            self.upload_data(param, search_key)
            print(f'爬取第{i}个商品  完成')
            sleep(2)
            driver.back()

    def upload_data(self, param, search_key):
        """
        上传数据
        Args:
            param:

        Returns:

        """
        try:
            param_data = {
                    'source':          2,
                    'keyword':         search_key,
                    'collection_data': json.dumps(param)
            }
            _res = requests.post(self.api_url + '/api/collection/warehousing?source&collection_data',
                                 data = param_data)
            print(_res.text)
            res_j = json.loads(_res.text)
            if res_j['status_code'] == 0:
                print("数据上传完成...")
            else:
                print("数据上传失败, 进入下一商品采集...")
        except Exception as e:
            print(f"上传数据失败 => {e}")

    def time_end(self, second = 10):
        count = 0
        while (count < second):
            count_now = second - count
            print("\r", f'倒计时还有{count_now}秒', flush = True, end = "", )
            time.sleep(1)
            count += 1


PDD = PDD()

if __name__ == '__main__':
    try:
        PDD.spider_PDD(PDD.login_PDD(PDD.browser_initial()))
    except:
        PDD.get_cookie_PDD()
        PDD.spider_PDD(PDD.login_PDD(PDD.browser_initial()))
