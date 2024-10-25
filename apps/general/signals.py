import os

from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save, pre_delete
from django.db.models import ImageField, FileField, TextField, CharField


@receiver(post_delete)
def delete_related_field(instance, sender, *kwargs):
    """ delete related files from all models on delete"""
    print("--------------------------------------------")
    for field in sender._meta.get_fields():
        # for field in instance.__class__._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file = getattr(instance, field.name)
            if file and os.path.exists(file.path):
                os.remove(file.path)


@receiver(pre_save)
def update_related_field(instance, sender, *kwargs):
    """ update related files from all models on update"""
    print("////////////////////////////")
    for field in sender._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            old_file = getattr(instance, field.name)
            new_file = getattr(instance, field.name)
            if old_file and old_file != new_file and os.path.exists(old_file.path):
                os.remove(old_file.path)



            # if not file and os.path.exists(file.path):
            #     os.remove(file.path)

        # for field in instance.__class__._meta.get_fields():

@receiver(pre_save)
def normalize_text(instance, **kwargs):
    print("============================")
    for field in instance._meta.get_fields():
        if isinstance(field, (TextField, CharField)):
            value = getattr(instance, field.name)
            setattr(instance, field.name, ' '.join(value.split()))
