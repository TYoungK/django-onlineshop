from django.contrib import admin
from .models import *
# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_diplay = ['code','use_from','use_to','amount']
    list_filter = ['active','use_from','use_to']
    search_fields = ['code']

admin.site.register(Coupon,CouponAdmin)
