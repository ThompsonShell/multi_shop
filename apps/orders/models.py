from django.db import models
from django.conf import settings
from apps.coupons.models import Coupon
from apps.general.models import PaymentMethod


class Order(models.Model):
    """
    <<<<<<<<< this model work for orders >>>>>>>>>
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    payment_method = models.ForeignKey('general.PaymentMethod', on_delete=models.PROTECT)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True,
                                blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(
                                max_digits=10,
                                decimal_places=2,
                                default=0
                            )
    delivery_price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0)
    total_price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0)
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT)


    def __str__(self):
            return self.user


class OrderProduct(models.Model):
    """
    <<<<<<<< this model work for ordered product >>>>>>>>
    """

    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(to='orders.Order',
                                on_delete=models.PROTECT)
    product = models.ForeignKey(to='products.Product',
                                on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0)

