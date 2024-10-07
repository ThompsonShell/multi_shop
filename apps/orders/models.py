from django.db import models

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    # payment_method = models.ForeignKey()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=True)
    # coupon = models.ForeignKey()
    coupon_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_code = models.CharField(max_length=20)