from django.shortcuts import redirect
from django.utils.translation import activate, get_language

from config import settings


# Create your views here.
def set_language(request, lang):
    if not lang in settings.MODELTRANSLATION_LANGUAGES:
        lang = settings.LANGUAGE_CODE
    old_lang = get_language()
    activate(lang)
    host= request.build_absolute_uri('/')
    redirect_to=host + lang + request.META['HTTP_REFERER'].replace(host, '')[2:]
    return redirect(redirect_to)
