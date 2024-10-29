from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.comments.models import ProductComment


# Register your models here.
@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message')

# Agar TranslationAdmin ishlatmoqchi bo'lsangiz:
# @admin.register(ProductComment)
# class ProductCommentAdmin(TranslationAdmin):
#     list_display = ('id', 'comment', 'user', 'created_at', 'updated_at', 'message')
