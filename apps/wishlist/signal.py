from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.wishlist.models import Wishlist


@receiver((post_save, post_delete), sender=Wishlist)
def wishlist_post_save(instance:Wishlist, **kwargs):
    instance.user.wishlist_count = Wishlist.objects.filter(user_id=instance.user_id).count()