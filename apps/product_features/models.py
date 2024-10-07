from django.db import models

from apps.products.models import Product
from apps.feature_values.models import FeatureValue

class ProductFeatures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE)