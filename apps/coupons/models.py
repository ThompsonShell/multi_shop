from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)