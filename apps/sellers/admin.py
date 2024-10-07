from django.contrib import admin


from apps.sellers.models import Seller, SellerDetail

class SellerDetailInline(admin.TabularInline):
    model = SellerDetail

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    inlines = [
        SellerDetailInline,
    ]
