import os

from django.db.models import TextField, CharField
from django.dispatch import receiver
from apps.abouts.models import About
from django.db import models
from django.db.models.signals import (
    pre_save, pre_init,
    post_save, pre_delete,
    post_delete, post_init
)

#
# @receiver(pre_save, sender=About)
# def normalize_text(instance, **kwargs):
#     print("============================")
#     for field in instance._meta.get_fields():
#         if isinstance(field, (TextField, CharField)):
#             value = getattr(instance, field.name)
#             setattr(instance, field.name, ' '.join(value.split()))

# @receiver(post_delete, sender=About)
# def delete_related_image(instance,**kwargs):
#     print("image successful deleted")
#     os.remove(instance.image.path)