from django.conf import settings
from django.db import models

from apps.products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    product = models.ForeignKey(
        to='products.Product',
        on_delete=models.PROTECT
    )

    class Meta:
        unique_together = ["user", "product"]
