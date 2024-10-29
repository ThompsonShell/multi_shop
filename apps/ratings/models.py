from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProductRating(models.Model):
    # <<< this model create product rating >>>
    product = models.ForeignKey('products.Product',related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
