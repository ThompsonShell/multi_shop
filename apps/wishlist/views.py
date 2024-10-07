from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from apps.products.models import Product
from apps.wishlist.models import Wishlist


def wishlist(request: WSGIRequest):
    context = {"wishlists": Wishlist.objects.select_related('user', 'product')}
    return render(request=request, template_name='wishlist.html', context=context)


@login_required
def create_wishlist(request: WSGIRequest, product_id: int):
    if not Product.objects.filter(id=product_id).exists():
        return redirect('products')
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product_id=product_id)
    return redirect('products:product_list')


@login_required
def delete_wishlist(request: WSGIRequest, _id: int):
    Wishlist.objects.filter(id=_id).delete()
    return redirect('wishlist')
