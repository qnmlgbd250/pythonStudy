# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 14:06
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : GetPath.py
# @Software: PyCharm

import re
import os
import sys

sys.path.append("/home/brady/python_project/new_platform_master")

from python_test.public.Error import PathError

# 项目名
prj_folder_names = ['python_test', 'data', 'new_platform_master']
def get_project_path() -> str:
    """
    取当前项目根目录的绝对路径
    """

    for folder_name in prj_folder_names:
        # 根据启动的文件寻找根目录路径
        match = re.search('.+?' + folder_name, os.path.dirname(os.path.realpath(sys.argv[0])))
        if match:
            project_path = match.group()
            return project_path
        # 根据当前文件寻找根目录
        match = re.search('.+?' + folder_name, os.path.dirname(os.path.realpath(__file__)))
        if match:
            project_path = match.group()
            return project_path
    else:
        raise PathError


def get_desktop():
    """
    获取Windows系统桌面
    :return:
    """
    import win32api, win32con
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                              r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', 0, win32con.KEY_READ)
    return win32api.RegQueryValueEx(key, 'Desktop')[0]
