from django.contrib import admin

from apps.products.models import Product, ProductFeatures


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeatures
    min_num = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureInline]
    readonly_fields = ('price', 'old_price')
