import requests

header = {

        'Connection':         'keep-alive',
        'Content-Length':     '0',
        'Pragma':             'no-cache',
        'Cache-Control':      'no-cache',
        'sec-ch-ua':          '"NotA;Brand";v="99","Chromium";v="96","MicrosoftEdge";v="96"',
        'sec-ch-ua-mobile':   '?0',
        'User-Agent': 'yuanrenxue.project',
        'sec-ch-ua-platform': '"Windows"',
        'Accept':             '*/*',
        'Origin':             'https://match.yuanrenxue.com',
        'Sec-Fetch-Site':     'same-origin',
        'Sec-Fetch-Mode':     'cors',
        'Sec-Fetch-Dest':     'empty',
        'Referer':            'https://match.yuanrenxue.com/match/3',
        'Accept-Encoding':    'gzip,deflate,br',
        'Accept-Language':    'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie':             'sessionid=z77lik6rru4szxjzzl5avg50h79f69t8',
}
s = requests.session()
s.headers = header

def get(p):
    res = s.get('https://match.yuanrenxue.com/jssm')
    print(res)
    url = f'https://match.yuanrenxue.com/api/match/3?page={p}'
    ress = s.get(url)
    print(ress.json())
    return ress.json()

if __name__ == '__main__':
    sum_ = 0
    for page_num in range(1, 6):
        res = get(page_num)
        for i in res['data']:
            sum_ += i['value']
    print(sum_)
