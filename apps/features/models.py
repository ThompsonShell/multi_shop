from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=255)