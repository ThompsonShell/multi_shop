import os

from django.dispatch import receiver
from apps.abouts.models import About
from django.db import models
from django.db.models.signals import (
    pre_save, pre_init,
    post_save, pre_delete,
    post_delete, post_init
)




@receiver(post_delete, sender=About)
def delete_related_image(instance,**kwargs):
    os.remove(instance.image.path)