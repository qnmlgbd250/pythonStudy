# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 14:25
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 多线程模板.py
# @Software: PyCharm
import requests
from lxml import etree
import os
from threading import Thread
from queue import Queue
from urllib import parse

class CrawlInfo(Thread):
    def __init__(self,url_queue,html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue
    def run(self):
        while self.url_queue.empty() == False:
            url = self.url_queue.get()
            resp1 = requests.get(url=url, headers=headers)
            # 处理中文乱码问题
            resp1_text = resp1.text.encode('ISO-8859-1').decode('utf-8')
            if resp1.status_code == 200:
                self.html_queue.put(resp1_text)

class ParseInfo(Thread):
    def __init__(self,html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue
    def run(self):
        while self.html_queue.empty() == False:
            tree1 = etree.HTML(self.html_queue.get())
            page_n = int(tree1.xpath('//*[@id="pageNum"]/a[1]/text()')[0][1:-3])
            title = tree1.xpath('/html/head/title/text()')[0]
            href0 = tree1.xpath('/html/head/link[2]/@href')[0]
            title_path = m_path + f'/{title}'
            if not os.path.exists(title_path):
                os.mkdir(title_path)
            for i in range(1, page_n + 1):
                if i == 1:
                    every_href = href0
                else:
                    every_href = href0.replace('.html', f'_{i}.html')
                resp2 = requests.get(url=every_href, headers=headers)
                # 处理中文乱码问题
                resp2_text = resp2.text.encode('ISO-8859-1').decode('utf-8')
                tree2 = etree.HTML(resp2_text)
                src_list = tree2.xpath('/html/body/div[6]//@src')
                for src in src_list:
                    jpg_data = requests.get(url=src, headers=headers).content
                    jpg_name = src.split("/")[-1]
                    name_path = title_path + f'/{jpg_name}'
                    with open(name_path, 'wb') as fp:
                        fp.write(jpg_data)
                        print(jpg_name, '下载完成')


if __name__ == '__main__':
    url_queue = Queue()
    html_queue=Queue()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    kw = 'xxx'
    keyword = parse.quote(kw, encoding='utf-8')
    url0 = ''
    resp = requests.get(url=url0, headers=headers).text
    tree = etree.HTML(resp)
    href_list = list(set(tree.xpath('//*[@id="load-img"]/ul//@href')))
    m_path = './图图岛'
    if not os.path.exists(m_path):
        os.mkdir(m_path)

    for href in href_list:
        url_queue.put(href)

    crawl_list = []
    for i in range(5):
        Crawl = CrawlInfo(url_queue, html_queue)
        crawl_list.append(Crawl)
        Crawl.start()

    for crawl in crawl_list:
        crawl.join()

    parse_list = []
    for i in range(5):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()

    for parse in parse_list:
        parse.join()