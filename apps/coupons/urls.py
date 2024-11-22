from django.urls import path


from apps.coupons.views import check_coupon

app_name = 'coupons'



urlpatterns = [
    path('check/', check_coupon, name='check_coupon'),
]
