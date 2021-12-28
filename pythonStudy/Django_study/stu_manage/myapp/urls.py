# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 17:14
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name = "index"),
        path('users', views.indexUsers, name = "users"),  # 浏览用户信息
        path('users/add', views.addUsers, name = "addusers"),  # 加载添加用户信息表单
        path('users/insert', views.insertUsers, name = "insertusers"),  # 执行用户信息添加
        path('users/<int:uid>/del', views.delUsers, name = "delusers"),  # 执行用户信息删除
        path('users/<int:uid>/edit', views.editUsers, name = "editusers"),  # 加载用户信息编辑表单
        path('users/update', views.updateUsers, name = "updateusers"),  # 执行用户信息编辑
        # path('addtest', views.inserttext)
]
