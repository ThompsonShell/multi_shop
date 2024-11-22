from django.contrib import admin

from apps.coupons.models import Coupon


# Register your models here.
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False