from django.contrib import admin

from apps.general.models import General


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ["phone1",
                    "phone2",
                    "address",
                    "logo",
                    ]
