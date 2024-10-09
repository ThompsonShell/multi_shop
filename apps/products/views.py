from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.products.models import Product


def product_list(request: WSGIRequest) -> HttpResponse:
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)
    paginate_obj = Paginator(Product.objects.order_by('-pk'), 9)
    page_obj = paginate_obj.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request=request, template_name='shop.html', context=context)

