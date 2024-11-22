from django.shortcuts import render, redirect

from apps.carts.models import Cart
from apps.general.models import General


def checkout(request):
    carts = Cart.objects.filter(user=request.user).select_related('product')
    if not carts:
        return redirect('cart-page')

    try:
        shipping_percent = General.objects.first().shipping_percent
    except AttributeError:
        shipping_percent = 0


    context = {
        'carts': carts,
        'shipping_percent': shipping_percent,
        'total_cart': sum([cart.quantity * cart.product.price for cart in carts]),
    }
    return render(request=request, template_name='checkout.html',context=context)

