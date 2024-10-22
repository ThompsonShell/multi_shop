import os
from modeltranslation.utils import get_translation_fields
from django.dispatch import receiver
from apps.abouts.models import About
from django.db import models
from django.db.models.signals import (
    pre_save, pre_init,
    post_save, pre_delete,
    post_delete, post_init
)


@receiver(pre_save, sender=About)
def normalize_text(instance, **kwargs):
    title_fields = get_translation_fields('title')
    description_fields = get_translation_fields('description')

    for field in title_fields:
        value = getattr(instance, field, None)
        if value:
            normalized_value = ' '.join(value.split())
            setattr(instance, field, normalized_value)

    for field in description_fields:
        value = getattr(instance, field, None)
        if value:
            normalized_value = ' '.join(value.split())
            setattr(instance, field, normalized_value)


@receiver(post_delete, sender=About)
def delete_related_image(instance,**kwargs):
    print("image successful deleted")
    os.remove(instance.image.path)