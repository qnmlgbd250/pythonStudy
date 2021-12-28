import requests
import json
import time
import base64


class GP(object):
    def __init__(self):
        super(GP, self).__init__()
        self._header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.106 Safari/537.36',
        }
        self.url = 'https://futsse.eastmoney.com'
        self.s = {
            '黄金': 'U',
            '白银': 'G'
        }

    def TD(self, r):
        y = self.s.get(r, '未知状态')
        res = requests.get(self.url + f'/static/118_A{y}TD_qt?', headers = self._header)
        info = json.loads(res.text.replace('aa(', '').replace(')', ''))
        qt = info['qt']
        data = {
            '涨幅': qt['zdf'],
            '总量': qt['vol'],
            '最高': qt['h'],
            '昨收': qt['qrspj'],
            '最新': qt['p'],
            '涨跌额': qt['zde'],
            '最低': qt['l'],
            '外盘': qt['wp'],
            '内盘': qt['np'],
            '前结': qt['zjsj'],
            '日增': qt['rz'],
            '今开': qt['o'],
            '持仓量': qt['ccl'],
        }
        param = {
            '时间': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
            '数据': data
        }
        with open(f'{r} T+D .txt', 'a+', encoding = 'utf-8') as f:
            f.write(str(param) + '\n')
            print(f'{r}写入数据完成...')

    def time_end(self, a = 24 * 60 * 60):
        count = 0
        while (count < a):
            count_now = a - count
            print("\r", f'倒计时{count_now}秒', end = "", flush = True)
            time.sleep(1)  # sleep 1 second
            count += 1


GP = GP()

if __name__ == '__main__':
    bs1 = input('请输入密钥1: ')
    debs64 = base64.b64decode(bs1)
    debs64 = debs64.decode('utf-8')
    GP.TD(debs64)
    bs1 = input('请输入密钥2: ')
    debs64 = base64.b64decode(bs1)
    debs64 = debs64.decode('utf-8')
    GP.TD(debs64)
    GP.time_end()
