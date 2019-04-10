from django.db import models
from main import models as mm

class Passenger(mm.User):
    user_type_choice = (
        ('passenger', '乘客'),
    )

    user_type = models.CharField(choices=user_type_choice, max_length=64, default='passenger', verbose_name='用户类型')
    order_num = models.CharField(max_length=64, verbose_name='订单号')

    class Meta:
        verbose_name = '乘客'
        verbose_name_plural = '乘客'




