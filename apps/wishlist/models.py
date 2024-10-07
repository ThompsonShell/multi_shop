from django.conf import settings
from django.db import models

from apps.products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "product"]

    def __str__(self):
        return f"{self.user.username}"