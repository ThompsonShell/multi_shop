from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from apps.products.models import Product
from apps.wishlist.models import Wishlist


@login_required
def wishlist(request: WSGIRequest):
    context = {"wishlists": Wishlist.objects.filter(user=request.user).select_related('product')}
    return render(request=request, template_name='wishlist.html', context=context)


@login_required
def create_wishlist(request: WSGIRequest, product_id: int):
    if not Product.objects.filter(id=product_id).exists():
        return redirect('products')
    Wishlist.objects.get_or_create(user=request.user, product_id=product_id)
    return redirect('products:product_list')


@login_required
def delete_wishlist(request: WSGIRequest, product_id: int) -> None:
    Wishlist.objects.filter(id=product_id).delete()
    return redirect('wishlist')
