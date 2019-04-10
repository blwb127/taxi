from django.contrib import admin
from .models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ('user_type', 'user_name', 'password', 'email', 'sex', 'user_num',
                    'live_place', 'phone', 'birthday', 'status','job_num', 'car_name', 'id_num',)

admin.site.register(Driver, DriverAdmin)