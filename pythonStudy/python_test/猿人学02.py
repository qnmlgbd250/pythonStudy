import requests
import execjs
import time

def get_res(page_num,parm):
    url = 'https://match.yuanrenxue.com/api/match/2?page={}'.format(page_num)
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookie': parm
    }
    response = requests.get(url=url,headers=headers)
    print(response.content.decode())
    return response.json()

def calculate_m_value():
    with open('test.js',mode='r',encoding='utf-8') as f:
        JsData = f.read()
    cookie_value = execjs.compile(JsData).call('get_cookie')
    return cookie_value

if __name__ == '__main__':
    sum_ = 0
    for page_num in range(1,6):
        print(page_num)
        time.sleep(1)
        cookie_value = calculate_m_value()
        print(cookie_value)
        res = get_res(page_num,cookie_value)
        for i in res['data']:
            sum_ +=i['value']
    print(sum_)


