# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 14:06
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : apple.py
# @Software: PyCharm
import requests

headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
           'cookie': 'cna=QwB/Geb80zcCAXjlW12Xj/LN; t=138cf80a72705b654ca911e8d5a172ef; sgcookie=E100pNaDiPckbAyb2%2FCbnAUkquJvekIqMvb%2BRtXMd9ai79VJyYuSpbT3zRSVqGx7fcjngJ8cYCymrJpI0JhtLFfqBrPORm2xZ9m16xKP4D5imYfj2NcUjyYcunbvYRvy5Fc4; uc3=id2=UUkHLz1gJPed6Q%3D%3D&nk2=p2Mto1vJEArY&lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dCvUFgLXO83gltx14%3D; lgc=%5Cu58A8%5Cu5DF2%5Cu6210%5Cu60B2s; uc4=id4=0%40U2uL4QMCokRYxSwaGKsQRM2DcFOD&nk4=0%40pVX6IsL6XuUNNNXgP271LJpddMk%3D; tracknick=%5Cu58A8%5Cu5DF2%5Cu6210%5Cu60B2s; _cc_=V32FPkk%2Fhw%3D%3D; thw=cn; mt=ci=-1_0; _tb_token_=33aee76ebb97b; _m_h5_tk=bb185998147eb6168baaa0f606afc62b_1647158447551; _m_h5_tk_enc=9f1859197fbee944bc4c964911b1dead; cookie2=12cae73e41b9a2c3d9fb18684bfcd3ba; _samesite_flag_=true; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaMouseten=null; ariaStatus=false; lLtC1_=1; miid=5846137181556746429; enc=sEgfSj%2FXODXnzHDu0s5BYEWwCblr2b3bsXBeFMmxk46kL%2BiEPjxsQPNo9GziQBuYSQuyE3%2FD34IfeUYU6abjaQ%3D%3D; uc1=cookie14=UoewB%2FOeK0biSg%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; ext_pgvwcount=-0.1; l=eBaWu1Z4gsoCSKFLBO5alurza77TWERfcsPzaNbMiIncC6j16-JiagAQ0WDyYpKRR8XcG3Yp4sxyEyeTRF_uJsuKHdGJ4AadZ3ivQef..; isg=BFZW-PDYKAyHvB_LMoXVqB6tpwxY95oxEl4KzsCnuTiyg_4dKYXoQe0xGx9vK5JJ; JSESSIONID=88871B191FCBE20BA30186CB5C0946F4',
           'referer': 'https://s.taobao.com/',
           'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"', 'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'script', 'sec-fetch-mode': 'no-cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}


def apple_():
    for page in range(1, 2):
        import time
        time_ = str(time.time() * 1000)
        time__ = time_.split('.')
        print(f'当前页面{page}')
        params = {'data-key': 's',
                  'data-value': str(44 * page),
                  'ajax': 'true',
                  '_ksTS': f'{time__[0]}_{time__[1]}',
                  'callback': f'jsonp{str(int(time__[1]) + 1)}',
                  'spm': 'a21bo.jianhua.201867-main.15.5af911d9GoThXX',
                  'q': '手机',
                  'cps': 'yes',
                  'ppath': '20000:30111',
                  'bcoffset': '0',
                  'p4ppushleft': f',44',
                  's': str(44 * (page - 1))
                  }
        print(params)

        date_ = requests.get('https://s.taobao.com/search?', headers = headers, params = params).text
        print(date_)
        import re
        import json
        json_data = re.findall(r'"itemlist":(.*),"bottomsearch":', date_)[0]
        dict_data = json.loads(json_data)
        auctions = dict_data['data']['auctions']
        rows = []
        for auction in auctions:
            seller_name = auction['nick']
            phone_type = auction['raw_title']
            phone_price = auction['view_price']
            row = [seller_name, phone_type, phone_price]
            rows.append(row)
        print(rows)
        with open('apple_taobao.txt', 'a+') as file:
            for row in rows:
                file.write(' '.join([str(item) for item in row]))
                file.write('\n')


if __name__ == '__main__':
    apple_()




