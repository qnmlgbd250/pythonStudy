# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 10:08
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : gui002.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(750, 400, 1000, 750)
        # 设置窗口的标题
        self.setWindowTitle('大屏自动签到')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('320.jpg'))

        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())