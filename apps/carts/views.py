from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.shortcuts import render, redirect, get_object_or_404

from apps.carts.models import Cart


def cart(request):
    if not request.user.is_authenticated:
        return redirect('login-page')

    queryset = Cart.objects.annotate(total_price=F('queryset') * F('product__price'),).filter(user=request.user)

    context = {
        'user_carts': queryset.select_related('product'),
        'cart_total_price': queryset.aggregate(Sum('total_price')),
    }
    return render(request, 'cart.html', context)

@login_required(login_url='login-page')
def create_cart(request, product_id: int):
    quantity = request.POST.get('cart_quantity', 1)
    print(quantity)
    print("============")
    obj, created = Cart.objects.get_or_create(product_id=product_id, user=request.user)

    if obj.quantity != quantity:
        obj.quantity = quantity
        print(quantity)

        obj.save()
    return redirect(request.META['HTTP_REFERER'])


def delete_cart(request, product_id: int):
    Cart.objects.filter(product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def set_cart_quantity(request, cart_id: int):
    if request.method != 'POST':
        return redirect('home-page')
    cart_obj = get_object_or_404(Cart, pk=cart_id)
    quantity = request.POST.get('item_quantity', cart_obj.quantity)

    if quantity.isdigit() and int(quantity) <= 0:
        cart_obj.delete()
    else:
        cart_obj.quantity = quantity
        cart_obj.save()
    return redirect(request.META['HTTP_REFERER'])