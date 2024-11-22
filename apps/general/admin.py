from django.contrib import admin
from django.contrib.auth.models import User

from apps.general.models import General, PaymentMethod


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ["phone1",
                    "phone2",
                    "address",
                    "logo",
                    "shipping_percent"
                    ]

    def has_add_permission(self, request):
        return not General.objects.exists()

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ["name",]