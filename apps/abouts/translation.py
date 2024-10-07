from modeltranslation.translator import TranslationOptions, register

from apps.abouts.models import About


@register(About)
class AboutsTranslationOptions(TranslationOptions):
    fields = ('title','description')
