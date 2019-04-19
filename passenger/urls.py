#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: ??
@author: lyj
@site: 
@software: PyCharm
@file: urls.py
@time: 2019/3/26 0026 20:43
"""

from django.conf.urls import url
from django.contrib import admin
from passenger import views as p_views

urlpatterns = [
    url(r'^login/', p_views.login),
    url(r'^register/', p_views.register),
    url(r'^logout/', p_views.logout),
    url(r'^index/', p_views.index),
    url(r'^profile/', p_views.accounts_profile),
]

