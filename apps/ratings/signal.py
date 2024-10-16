from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from apps.ratings.models import ProductRating
from apps.products.models import Product


@receiver([post_save,post_delete], sender=ProductRating)
def product_rating_post_save(instance:ProductRating,**kwargs):
    instance.product.set_avg_rating()