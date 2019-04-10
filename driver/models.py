from django.db import models
from main import models as mm


class Driver(mm.User):
    user_type_choice = (
        ('driver', '司机'),
    )

    user_type = models.CharField(choices=user_type_choice, max_length=64, default='driver', verbose_name='用户类型')
    job_num = models.CharField(max_length=64, verbose_name='司机工号')
    car_name = models.CharField(max_length=64, verbose_name='车牌号')
    id_num = models.CharField(max_length=64, verbose_name='司机身份证号')

    class Meta:
        verbose_name = '司机'
        verbose_name_plural = '司机'







