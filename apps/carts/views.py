from itertools import product

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.carts.models import Cart


def cart(request):
    if not request.user.is_authenticated:
        return redirect('login-page')
    context = {
        'user_carts': Cart.objects.filter(user=request.user).select_related('product')
    }
    return render(request, 'cart.html', context)

@login_required(login_url='login-page')
def create_cart(request, product_id: int):
    quantity = request.GET.get('cart_quantity', 1)

    obj, created = Cart.objects.get_or_create(product_id=product_id, user=request.user)

    if obj.quantity != quantity:
        obj.quantity = quantity
        obj.save()
    return redirect(request.META['HTTP_REFERER'])


def delete_cart(request, product_id: int):
    Cart.objects.filter(product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])