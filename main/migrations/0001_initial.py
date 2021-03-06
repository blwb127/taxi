# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-19 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=64, verbose_name='订单号')),
                ('price', models.CharField(max_length=64, verbose_name='价格')),
                ('number', models.CharField(max_length=64, verbose_name='人数')),
                ('first_place', models.CharField(default='', max_length=64, verbose_name='出发地')),
                ('last_place', models.CharField(default='', max_length=64, verbose_name='目的地')),
            ],
            options={
                'verbose_name': '订单处理',
                'verbose_name_plural': '订单处理',
            },
        ),
    ]
