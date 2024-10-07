from modeltranslation.translator import TranslationOptions, register

from apps.categories.models import Category


@register(Category)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)
