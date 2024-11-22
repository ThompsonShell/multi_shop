from django.db import models
from django.conf import settings
from datetime import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    from_coupon = models.BooleanField(default=False)
    to_coupon = models.BooleanField(default=False)
    expiration_date = models.DateTimeField()
    discount_percent = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )


class UsedCoupon(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def check_coupon_date(self):
        return self.expiration_date <= timezone.now()

    def __str__(self):
        return self.title