import requests

from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.db import models
from django.core.cache import cache


from apps.general.validation_phone import validate_phone


class General(models.Model):
    class Currency(models.TextChoices):
        USD = 'USD', 'USD'
        UZS = 'UZS', 'UZS'
        RUB = 'RUB', 'RUB'

    DEFAULT_CURRENCY = Currency.UZS

    phone1 = models.CharField(max_length=13, validators=[validate_phone], help_text="UZB Number +998123456789")
    phone2 = models.CharField(max_length=13, null=True, blank=True, validators=[validate_phone])

    address = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to="general/logo/image/%Y/%m/%d/")

    def clean(self):
        if self.pk and General.objects.exists():
            raise ValidationError('Unique')


class GeneralSocialMedia(models.Model):
    url = models.URLField()
    icon = models.ImageField(upload_to="social_links/icon/image/%Y/%m/%d/")


class CurrencyAmount(models.Model):
    GET_CURRENCY_URL = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{currency}/all/{date}/'
    print(GET_CURRENCY_URL)
    currency = models.CharField(max_length=10, choices=General.Currency.choices)
    usd_amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()

    @classmethod
    def get_amount(cls, currency: str):
        print(currency)
        today = now().date()

        amount_in_uzs = cache.get(f'{currency}_{today}')
        if not amount_in_uzs:
            obj, created = cls.objects.get_or_create(
                currency=currency,
                date=today,
                defaults={
                    'usd_amount': requests.get(url=cls.GET_CURRENCY_URL.format(
                        currency=currency, date=today
                    )).json()[0]['Rate']
                }
            )
            cache.set(f'{currency}_{today}', obj.usd_amount)
            amount_in_uzs = obj.usd_amount
        print(amount_in_uzs)
        return amount_in_uzs

    class Meta:
        unique_together = (('currency', 'date'),)
