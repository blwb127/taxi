from django.contrib.auth.models import User
from django.db import models


class User(models.Model):

    user_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '空闲'),
        (3, '忙碌'),
    )

    gender = (
        ('male', "男"),
        ('male', "女"),
    )
    user_name = models.CharField(max_length=64, unique=True, verbose_name='用户名称')
    password = models.CharField(max_length=256, verbose_name='用户密码')
    email = models.EmailField(unique=True, verbose_name='用户邮箱')
    sex = models.CharField(max_length=32, choices=gender, default="男", verbose_name='用户性别')
    user_num = models.CharField(max_length=128, unique=True, verbose_name='用户序列号')
    live_place = models.CharField(max_length=64, verbose_name='用户住址')
    phone = models.CharField(max_length=64, verbose_name='用户电话')
    birthday = models.CharField(max_length=64, verbose_name='用户生日')

    status = models.SmallIntegerField(choices=user_status, default=0, verbose_name='用户状态')

    def __str__(self):
        return '<%s> %s' % (self.get_user_type_display(), self.user_name)


    class Meta:
        verbose_name = '用户总表'
        verbose_name_plural = '用户总表'
        abstract = True

class OrderZone(models.Model):
    order_num = models.CharField(max_length=64, verbose_name='订单号')
    price = models.CharField(max_length=64, verbose_name='价格')
    number = models.CharField(max_length=64, verbose_name='人数')
    first_place = models.CharField(max_length=64, default='',verbose_name='出发地')
    last_place = models.CharField(max_length=64, default='',verbose_name='目的地')

    class Meta:
        verbose_name = '订单处理'
        verbose_name_plural = '订单处理'











