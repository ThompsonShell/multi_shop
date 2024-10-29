from itertools import product, count

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.comments.models import ProductComment


@receiver((post_save, post_delete), sender=ProductComment)
def product_comment_post_save_or_post_delete(instance:ProductComment, *args, **kwargs):
    instance.product.comments_count = ProductComment.objects.filter(product_id=instance.product.id).count()
    instance.product.save()