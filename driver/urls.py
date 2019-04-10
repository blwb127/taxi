#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: ??
@author: lyj
@site: 
@software: PyCharm
@file: urls.py
@time: 2019/3/26 0026 20:24
"""
from django.conf.urls import url
from django.contrib import admin
from driver import views as d_views

urlpatterns = [
    url(r'^index/', d_views.index),
    url(r'^login/', d_views.login),
    url(r'^register/', d_views.register),
    url(r'^logout/', d_views.logout),
]


