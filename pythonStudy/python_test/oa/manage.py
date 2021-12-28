# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 14:53
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : manage.py
# @Software: PyCharm
import os

import click
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@click.group()
def main():
    """

    Returns:

    """
    import os
    os.environ.setdefault('LOAD_PROJECT_PATH', BASE_PATH)

@click.command()
@click.option('--sleep', "-on", help = "休眠时间", default = 5, type = int)
def oa_auto_sign(**kwargs):
    """自动签到"""
    from oa_auto_sign import OA_operat
    OA_operat(**kwargs).auto_sign_run()

@click.command()
@click.option('--sleep', "-on", help = "休眠时间", default = 5, type = int)
def oa_auto_soved(**kwargs):
    """自动标记"""
    from oa_auto_sign import OA_operat
    OA_operat(**kwargs).auto_sign_soved()

main.add_command(oa_auto_sign, name = 'sign')
main.add_command(oa_auto_soved, name = 'soved')

if __name__ == '__main__':
    main()