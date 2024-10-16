import os

from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.db.models import ImageField, FileField

@receiver(post_delete)
def delete_related_field(instance, sender, *kwargs):
    """ delete related files from all models on delete"""
    for field in sender._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file = getattr(instance, field.name)
            if file and os.path.exists(file.path):
                os.remove(file.path)