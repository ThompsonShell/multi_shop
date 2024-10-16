from django.db import models

from apps.products.models import Product


class Feature(models.Model):
    """this model create feature name


        For example:
        <<<<<<<<{'name': 'titanium metal', 'name':'operative'}>>>>>>>>>

    """

    name = models.CharField(max_length=255)


class FeatureValue(models.Model):
    """this model create feature feature and feature value


        For example:
        <<<<<<<<{'name': 'operative', 'value': '16GB'}>>>>>>>>>

    """
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class ProductFeatures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE)
