from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _, get_language
from django.db import models

from apps.sellers.choices import SocialLinkType


class Seller(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Male', _('Male')
        FEMALE = 'Female', _('Female')

    rating = models.IntegerField(verbose_name=_('rating'),
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    seller_gender = models.CharField(verbose_name=_('Gender'), max_length=10, choices=Gender.choices)

    @property
    def detail(self):
        obj = SellerDetail.objects.get(seller_id=self.pk, language=get_language())
        return {
            'name': obj.name,
            'description': obj.description,
        }


class SellerDetail(models.Model):
    class Language(models.TextChoices):
        EN = 'en',
        RU = 'ru',
        UZ = 'uz'

    seller = models.ForeignKey(to=Seller, on_delete=models.CASCADE)
    name  = models.CharField(verbose_name=_('name'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    language = models.CharField(verbose_name=_('language'), max_length=10, choices=Language.choices)


class SellerSocialLink(models.Model):
    social = models.PositiveSmallIntegerField(choices= SocialLinkType.choices)
    social_media = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.social_media
