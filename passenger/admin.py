from django.contrib import admin
from .models import Passenger


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('user_type', 'user_name', 'password', 'email', 'sex', 'user_num',
                    'live_place', 'phone', 'birthday', 'status',)

admin.site.register(Passenger, PassengerAdmin)