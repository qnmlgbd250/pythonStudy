# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 11:40
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 测试AL补全.py
# @Software: PyCharm
import schedule

class text():

    def job(self,name):
        print("her name is : ", name)

    def job2(self,name):
        print("111111111》》》 : ", name)

    def run(self):
        try:
            schedule.every(1).minutes.do(self.job2,name)
            schedule.every(2).minutes.do(self.job,name)
        except:
            schedule.every(1).minutes.do(self.job2, name)
            schedule.every(2).minutes.do(self.job, name)


name = "longsongpong"
# schedule.every(1).minutes.do(job2, name)
# schedule.every(2).minutes.do(job, name)  # 每隔十分钟执行一次任务
# schedule.every().hour.do(job, name)  # 每隔一小时执行一次任务
# schedule.every().day.at("10:30").do(job, name)  # 每天的10:30执行一次任务
# schedule.every(5).to(10).days.do(job, name)  # 每隔5到10天执行一次任务
# schedule.every().monday.do(job, name)  # 每周一的这个时候执行一次任务
# schedule.every().wednesday.at("13:15").do(job, name)  # 每周三13:15执行一次任务
text = text()
if __name__ == '__main__':
    text.run()
    while True:
        schedule.run_pending()
