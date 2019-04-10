from django.contrib import admin
from .models import OrderZone


class OrderZoneAdmin(admin.ModelAdmin):
    list_display = ('order_num', 'price', 'number','first_place', 'last_place',)


admin.site.register(OrderZone, OrderZoneAdmin)

