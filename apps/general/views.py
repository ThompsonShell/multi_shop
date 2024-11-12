from config import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest
from django.utils.translation import activate, get_language


from .models import General
from apps.products.models import Product


# Create your views here.
def set_language(request, lang):
    if not lang in settings.MODELTRANSLATION_LANGUAGES:
        lang = settings.LANGUAGE_CODE
    old_lang = get_language()
    activate(lang)
    host= request.build_absolute_uri('/')
    redirect_to=host + lang + request.META['HTTP_REFERER'].replace(host, '')[2:]
    return redirect(redirect_to)


def search(request: WSGIRequest)-> HttpResponse:
    print("<<<<<<<")
    search_text = request.GET.get('search_text', ' ')
    print(">>>>>>>>")
    request.session['search_text'] = search_text
    return redirect('products:product_list')



def set_currency(request, currency: str):
    currencies = General.Currency.values
    if currency in currencies:
        request.session['currency'] = currency
    return redirect(request.META['HTTP_REFERER'])


def clear_session(request):
    if request.method == 'POST':
        request.session.clear()
    return redirect('home-page')

def general_info(request):
    general = General.objects.first()  # Get the first instance, or adjust as needed
    return render(request, 'your_template.html', {'general': general})


def checkout(request):
    return render(request=request, template_name='checkout.html',context={'page':'pages'})


