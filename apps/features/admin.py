from django.contrib import admin

from apps.features.models import Feature, FeatureValue



class FeatureValueInlineAdmin(admin.TabularInline):
    model = FeatureValue
    min_num = 1

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    inlines = [FeatureValueInlineAdmin]

@admin.register(FeatureValue)
class FeatureValueAdmin(admin.ModelAdmin):
    pass

