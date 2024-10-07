from django.conf import settings
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'

LOCALE_PATHS = [
    settings.BASE_DIR / 'translation',
]

USE_I18N = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LANGUAGES = (
    ('uz', _('Uzbek')),
    ('en', _('English')),
    ('ru', _('Russian')),
)

MODELTRANSLATION_LANGUAGES = ('en', 'uz', 'ru')
