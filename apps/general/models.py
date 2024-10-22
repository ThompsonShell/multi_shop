from django.core.exceptions import ValidationError
from django.db import models

from .validation_phone import validate_phone


class General(models.Model):
    phone1 = models.CharField(max_length=13, validators=[validate_phone], help_text="UZB Number +998123456789")
    phone2 = models.CharField(max_length=13, null=True, blank=True, validators=[validate_phone])

    location = models.URLField()
    address = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to="general/logo/image/%Y/%m/%d/")

    def clean(self):
        if self.pk and General.objects.exists():
            raise ValidationError('Unique')


class GeneralSocialMedia(models.Model):
    url = models.URLField()
    icon = models.ImageField(upload_to="social_links/icon/image/%Y/%m/%d/")
