from django.contrib import admin

from apps.product_ratings.models import ProductRating


@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    pass
