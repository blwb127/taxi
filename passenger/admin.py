from django.contrib import admin
from .models import Passenger


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password','email',)

admin.site.register(Passenger, PassengerAdmin)