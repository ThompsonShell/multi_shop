from django.db import models

from apps.coupons.models import Coupon


class Order(models.Model):
    """
    <<<<<<<<< this model work for orders >>>>>>>>>
    """

    # hal payment yaratilmagan
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True,
                                blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(
                                max_digits=10,
                                decimal_places=2,
                                default=0)
    delivery_price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0)
    total_price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0)
    coupon_code = models.CharField(max_length=50,
                                null=True,
                                blank=True)
    coupon_price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=True,
                                blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(to='auth.User', on_delete=models.PROTECT)
    # payment_method = models.ForeignKey(to='PaymentMethod', on_delete=models.PROTECT)


def __str__(self):
        return self.user


class OrderProduct(models.Model):
    """
    <<<<<<<< this model work for ordered product >>>>>>>>
    """

    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(to='orders.Order',
                                on_delete=models.CASCADE)
    product = models.ForeignKey(to='products.Product',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0)

