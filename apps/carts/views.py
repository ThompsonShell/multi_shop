from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.shortcuts import render, redirect, get_object_or_404

from apps.carts.models import Cart
from apps.coupons.models import UsedCoupon
from apps.general.models import General


@login_required(login_url='user_login')
def cart(request):
    try:
        shipping_percent = General.objects.first().shipping_percent
    except AttributeError:
        shipping_percent = 0


    user = request.user
    code = request.session.get('coupon_code', {}).get('code')
    if code is None and UsedCoupon.objects.filter(coupon__code=code, user_id=user.pk).exists():
        del request.session['coupon_data']

    queryset = Cart.objects.annotate(total_price=F('quantity') * F('product__price')).filter(user=request.user)
    context = {
        'shipping_percent': shipping_percent,
        'user_carts': queryset.select_related('product'),
        'cart_total_price': queryset.aggregate(Sum('total_price'))['total_price__sum'],
    }
    context['total_price'] = context['cart_total_price'] + context['cart_total_price'] * shipping_percent / 100 - context['cart_total_price'] * request.session.get('coupon_code', {}).get('discount', 0 ) /100
    print()
    return render(request=request, template_name='cart.html', context=context)


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
