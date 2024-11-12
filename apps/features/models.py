from PIL.features import features
from django.db import models

from apps.products.models import Product


class Feature(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.PROTECT, related_name='values')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('feature', 'name'),)
