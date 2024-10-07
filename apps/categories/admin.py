from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name')
